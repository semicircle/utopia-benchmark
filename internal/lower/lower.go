// Package lower rewrites a canonical program so that a target dialect can
// express it with the same meaning. Constructs the dialect lacks are rebuilt
// from ones it has (down to labels and jumps), and semantic knobs such as the
// index base are compensated for.
package lower

import (
	"fmt"

	. "utopia/internal/lang"
)

type Options struct {
	// Raw skips semantic compensation (index base, loop bounds, switch
	// fallthrough). Documentation uses it to show a knob's raw effect.
	Raw bool
}

type frameKind uint8

const (
	frameNative frameKind = iota // the dialect's own loop: break/continue stay
	frameWhile                   // lowered into a while: continue runs post first
	frameGoto                    // lowered into labels
	frameSwitch
)

type frame struct {
	kind      frameKind
	breakL    string
	contL     string
	post      []Stmt
	usedBreak bool
	usedCont  bool
}

type lowerer struct {
	d        *Dialect
	raw      bool
	n        int
	frames   []*frame
	reserved map[string]bool
	err      error
}

// Lower rewrites prog (written in the canonical dialect) for dialect d.
func Lower(d *Dialect, prog *Program, opt Options) (*Program, error) {
	l := &lowerer{d: d, raw: opt.Raw, reserved: map[string]bool{}}
	for _, w := range d.Keywords {
		l.reserved[w] = true
	}
	for _, w := range d.Builtins {
		l.reserved[w] = true
	}
	out := &Program{}
	for _, f := range prog.Funcs {
		nf := &FuncDecl{Name: l.name(f.Name), Line: f.Line}
		for _, p := range f.Params {
			nf.Params = append(nf.Params, l.name(p))
		}
		nf.Body = l.block(f.Body)
		out.Funcs = append(out.Funcs, nf)
	}
	out.Main = l.block(prog.Main)
	if l.err != nil {
		return nil, l.err
	}
	return out, nil
}

// name renames identifiers that collide with the dialect's reserved words.
func (l *lowerer) name(n string) string {
	for l.reserved[n] {
		n += "_"
	}
	return n
}

func (l *lowerer) label(prefix string) string {
	l.n++
	return fmt.Sprintf("%s%d", prefix, l.n)
}

func (l *lowerer) fail(format string, args ...any) {
	if l.err == nil {
		l.err = fmt.Errorf(format, args...)
	}
}

func (l *lowerer) block(ss []Stmt) []Stmt {
	var out []Stmt
	for _, s := range ss {
		out = append(out, l.stmt(s)...)
	}
	return out
}

func (l *lowerer) push(f *frame) { l.frames = append(l.frames, f) }
func (l *lowerer) pop()          { l.frames = l.frames[:len(l.frames)-1] }

// loopFrame finds the innermost loop, refusing to cross a switch.
func (l *lowerer) loopFrame(what string) *frame {
	for i := len(l.frames) - 1; i >= 0; i-- {
		f := l.frames[i]
		if f.kind == frameSwitch {
			if what == "break" {
				l.fail("canonical programs may not use break inside a switch")
				return nil
			}
			continue
		}
		return f
	}
	l.fail("%s outside a loop", what)
	return nil
}

func (l *lowerer) stmt(s Stmt) []Stmt {
	switch s := s.(type) {
	case *Let:
		return []Stmt{&Let{Name: l.name(s.Name), Value: l.expr(s.Value), Line: s.Line}}
	case *Assign:
		return []Stmt{&Assign{Name: l.name(s.Name), Value: l.expr(s.Value), Line: s.Line}}
	case *IndexAssign:
		return []Stmt{&IndexAssign{Name: l.name(s.Name), Index: l.index(l.expr(s.Index)), Value: l.expr(s.Value), Line: s.Line}}
	case *CallStmt:
		return []Stmt{&CallStmt{Call: l.expr(s.Call).(*Call)}}
	case *Print:
		return []Stmt{&Print{Value: l.expr(s.Value), Newline: s.Newline, Line: s.Line}}
	case *Return:
		r := &Return{Line: s.Line}
		if s.Value != nil {
			r.Value = l.expr(s.Value)
		}
		return []Stmt{r}
	case *Break:
		f := l.loopFrame("break")
		if f == nil {
			return nil
		}
		if f.kind == frameGoto {
			f.usedBreak = true
			return []Stmt{&Goto{Label: f.breakL}}
		}
		return []Stmt{&Break{}}
	case *Continue:
		f := l.loopFrame("continue")
		if f == nil {
			return nil
		}
		switch f.kind {
		case frameGoto:
			f.usedCont = true
			return []Stmt{&Goto{Label: f.contL}}
		case frameWhile:
			return append(append([]Stmt(nil), f.post...), &Continue{})
		}
		return []Stmt{&Continue{}}
	case *Label, *Goto, *JumpIf, *Dispatch:
		l.fail("canonical programs may not use labels or jumps")
		return nil
	case *If:
		return l.ifStmt(s)
	case *Switch:
		return l.switchStmt(s)
	case *While:
		return l.loop(nil, s.Cond, nil, s.Body, s.Line, "while")
	case *CFor:
		var init, post []Stmt
		if s.Init != nil {
			init = l.stmt(s.Init)
		}
		if s.Post != nil {
			post = l.stmt(s.Post)
		}
		if l.d.Has(CCFor) {
			nf := &CFor{Cond: l.expr(s.Cond), Line: s.Line}
			if len(init) == 1 {
				nf.Init = init[0]
			}
			if len(post) == 1 {
				nf.Post = post[0]
			}
			nf.Body = l.native(s.Body)
			return []Stmt{nf}
		}
		return append(init, l.loop(nil, s.Cond, post, s.Body, s.Line, "for")...)
	case *CountFor:
		return l.countFor(s)
	case *DoWhile:
		return l.postTest(s.Body, s.Cond, false, s.Line)
	case *RepeatUntil:
		return l.postTest(s.Body, s.Cond, true, s.Line)
	}
	l.fail("lower: unknown statement %T", s)
	return nil
}

// native lowers a body that stays inside one of the dialect's own loops.
func (l *lowerer) native(body []Stmt) []Stmt {
	l.push(&frame{kind: frameNative})
	defer l.pop()
	return l.block(body)
}

// loop lowers a pre-test loop: while cond { body; post }.
func (l *lowerer) loop(pre []Stmt, cond Expr, post []Stmt, body []Stmt, line int, _ string) []Stmt {
	if l.d.Has(CWhile) {
		f := &frame{kind: frameWhile, post: post}
		if len(post) == 0 {
			f.kind = frameNative
		}
		l.push(f)
		b := l.block(body)
		l.pop()
		return append(pre, &While{Cond: l.expr(cond), Body: append(b, post...), Line: line})
	}
	top, cont, done := l.label("top"), l.label("next"), l.label("done")
	f := &frame{kind: frameGoto, breakL: done, contL: cont}
	if len(post) == 0 {
		f.contL = top
	}
	l.push(f)
	b := l.block(body)
	l.pop()
	out := append(pre, &Label{Name: top}, &JumpIf{Cond: negate(l.expr(cond)), Label: done})
	out = append(out, b...)
	if len(post) > 0 {
		if f.usedCont {
			out = append(out, &Label{Name: cont})
		}
		out = append(out, post...)
	}
	return append(out, &Goto{Label: top}, &Label{Name: done})
}

// postTest lowers do-while (until=false) and repeat-until (until=true).
func (l *lowerer) postTest(body []Stmt, cond Expr, until bool, line int) []Stmt {
	switch {
	case until && l.d.Has(CRepeatUntil):
		return []Stmt{&RepeatUntil{Body: l.native(body), Cond: l.expr(cond), Line: line}}
	case !until && l.d.Has(CDoWhile):
		return []Stmt{&DoWhile{Body: l.native(body), Cond: l.expr(cond), Line: line}}
	case until && l.d.Has(CDoWhile):
		return []Stmt{&DoWhile{Body: l.native(body), Cond: negate(l.expr(cond)), Line: line}}
	case !until && l.d.Has(CRepeatUntil):
		return []Stmt{&RepeatUntil{Body: l.native(body), Cond: negate(l.expr(cond)), Line: line}}
	}
	top, cont, done := l.label("top"), l.label("check"), l.label("done")
	f := &frame{kind: frameGoto, breakL: done, contL: cont}
	l.push(f)
	b := l.block(body)
	l.pop()
	again := l.expr(cond)
	if until {
		again = negate(again)
	}
	out := append([]Stmt{&Label{Name: top}}, b...)
	if f.usedCont {
		out = append(out, &Label{Name: cont})
	}
	out = append(out, &JumpIf{Cond: again, Label: top})
	if f.usedBreak {
		out = append(out, &Label{Name: done})
	}
	return out
}

func stepValue(e Expr) (int64, bool) {
	switch e := e.(type) {
	case nil:
		return 1, true
	case *IntLit:
		return e.V, true
	case *Unary:
		if lit, ok := e.X.(*IntLit); ok && e.Op == UNeg {
			return -lit.V, true
		}
	}
	return 0, false
}

func (l *lowerer) countFor(s *CountFor) []Stmt {
	step, ok := stepValue(s.Step)
	if !ok || step == 0 {
		l.fail("canonical count loops need a nonzero literal step")
		return nil
	}
	v := l.name(s.Var)
	if l.d.Has(CCountFor) {
		to := l.expr(s.To)
		if !l.raw && !l.d.Sem.CountInclusive {
			if step > 0 {
				to = add(to, 1)
			} else {
				to = add(to, -1)
			}
		}
		var st Expr
		if s.Step != nil {
			st = l.expr(s.Step)
		}
		return []Stmt{&CountFor{Var: v, From: l.expr(s.From), To: to, Step: st, Body: l.native(s.Body), Line: s.Line}}
	}
	// Evaluate the limit once, as the canonical loop does.
	var pre []Stmt
	limit := l.expr(s.To)
	if _, isLit := limit.(*IntLit); !isLit {
		t := l.label("_lim")
		pre = append(pre, &Let{Name: t, Value: limit})
		limit = &Ident{Name: t}
	}
	cmp := BLe
	if step < 0 {
		cmp = BGe
	}
	cond := &Binary{Op: cmp, L: &Ident{Name: v}, R: limit}
	inc := &Assign{Name: v, Value: &Binary{Op: BAdd, L: &Ident{Name: v}, R: &IntLit{V: step}}}
	if step < 0 {
		inc.Value = &Binary{Op: BSub, L: &Ident{Name: v}, R: &IntLit{V: -step}}
	}
	init := &Let{Name: v, Value: l.expr(s.From), Line: s.Line}
	if l.d.Has(CCFor) {
		return append(pre, &CFor{Init: init, Cond: cond, Post: inc, Body: l.native(s.Body), Line: s.Line})
	}
	return l.loop(append(pre, init), rawExpr{cond}, []Stmt{inc}, s.Body, s.Line, "count")
}

// rawExpr marks an expression that is already lowered.
type rawExpr struct{ Expr }

func (l *lowerer) ifStmt(s *If) []Stmt {
	if l.d.Has(CIf) {
		n := &If{HasElse: s.HasElse, Line: s.Line}
		for _, a := range s.Arms {
			n.Arms = append(n.Arms, CondArm{Cond: l.expr(a.Cond), Body: l.block(a.Body)})
		}
		if s.HasElse {
			n.Else = l.block(s.Else)
		}
		return []Stmt{n}
	}
	done := l.label("endif")
	var out []Stmt
	for i, a := range s.Arms {
		last := i == len(s.Arms)-1 && !s.HasElse
		next := done
		if !last {
			next = l.label("else")
		}
		out = append(out, &JumpIf{Cond: negate(l.expr(a.Cond)), Label: next, Line: s.Line})
		out = append(out, l.block(a.Body)...)
		if !last {
			out = append(out, &Goto{Label: done}, &Label{Name: next})
		}
	}
	if s.HasElse {
		out = append(out, l.block(s.Else)...)
	}
	return append(out, &Label{Name: done})
}

func terminal(body []Stmt) bool {
	if len(body) == 0 {
		return false
	}
	switch body[len(body)-1].(type) {
	case *Return, *Break, *Continue, *Goto:
		return true
	}
	return false
}

func (l *lowerer) switchStmt(s *Switch) []Stmt {
	l.push(&frame{kind: frameSwitch})
	defer l.pop()
	if l.d.Has(CSwitch) {
		n := &Switch{Subject: l.expr(s.Subject), HasDefault: s.HasDefault, Line: s.Line}
		addBreaks := !l.raw && l.d.Sem.SwitchFallthrough && l.d.Styles.Switch == StyleC
		for _, c := range s.Cases {
			body := l.block(c.Body)
			if addBreaks && !terminal(body) {
				body = append(body, &Break{})
			}
			n.Cases = append(n.Cases, Case{Values: c.Values, Body: body})
		}
		if s.HasDefault {
			n.Default = l.block(s.Default)
		}
		return []Stmt{n}
	}
	done := l.label("endcase")
	disp := &Dispatch{Subject: l.expr(s.Subject), Line: s.Line}
	var bodies []Stmt
	for i, c := range s.Cases {
		lbl := l.label("case")
		for _, v := range c.Values {
			disp.Entries = append(disp.Entries, DispatchEntry{Value: v, Label: lbl})
		}
		bodies = append(bodies, &Label{Name: lbl})
		body := l.block(c.Body)
		bodies = append(bodies, body...)
		lastBlock := i == len(s.Cases)-1 && !s.HasDefault
		if !lastBlock && !terminal(body) {
			bodies = append(bodies, &Goto{Label: done})
		}
	}
	if s.HasDefault {
		def := l.label("default")
		disp.Else = def
		bodies = append(bodies, &Label{Name: def})
		bodies = append(bodies, l.block(s.Default)...)
	} else {
		disp.Else = done
	}
	out := append([]Stmt{disp}, bodies...)
	return append(out, &Label{Name: done})
}

// ---- expressions ----

func (l *lowerer) expr(e Expr) Expr {
	switch e := e.(type) {
	case rawExpr:
		return e.Expr
	case *IntLit, *StrLit, *BoolLit, *NoneLit:
		return e
	case *ListLit:
		n := &ListLit{}
		for _, x := range e.Elems {
			n.Elems = append(n.Elems, l.expr(x))
		}
		return n
	case *Ident:
		return &Ident{Name: l.name(e.Name), Line: e.Line}
	case *Unary:
		return &Unary{Op: e.Op, X: l.expr(e.X)}
	case *Binary:
		n := &Binary{Op: e.Op, L: l.expr(e.L), R: l.expr(e.R), Line: e.Line}
		// When concatenation shares "+", an integer on the left would add
		// instead of concatenating, so convert it explicitly.
		if e.Op == BConcat && l.d.Ops.Concat == "+" && !stringy(n.L) && !stringy(n.R) {
			n.L = &Call{Name: l.d.Builtins[BStr], Builtin: BStr, Args: []Expr{n.L}}
		}
		return n
	case *Call:
		n := &Call{Name: e.Name, Builtin: e.Builtin, Line: e.Line}
		if e.Builtin == BNone {
			n.Name = l.name(e.Name)
		} else {
			n.Name = l.d.Builtins[e.Builtin]
		}
		for _, a := range e.Args {
			n.Args = append(n.Args, l.expr(a))
		}
		return n
	case *Index:
		return &Index{X: l.expr(e.X), I: l.index(l.expr(e.I)), Line: e.Line}
	}
	l.fail("lower: unknown expression %T", e)
	return e
}

// stringy reports whether an expression certainly yields a string.
func stringy(e Expr) bool {
	switch x := e.(type) {
	case *StrLit:
		return true
	case *Binary:
		return x.Op == BConcat
	case *Call:
		return x.Builtin == BStr || x.Builtin == BReadline
	}
	return false
}

// index converts a canonical 0-based index to the dialect's base.
func (l *lowerer) index(i Expr) Expr {
	if l.raw || l.d.Sem.IndexBase == 0 {
		return i
	}
	return add(i, int64(l.d.Sem.IndexBase))
}

// add returns e + k, folding literals and existing "+ literal" tails.
func add(e Expr, k int64) Expr {
	if k == 0 {
		return e
	}
	switch x := e.(type) {
	case *IntLit:
		return &IntLit{V: x.V + k}
	case *Binary:
		if lit, ok := x.R.(*IntLit); ok && (x.Op == BAdd || x.Op == BSub) {
			v := lit.V
			if x.Op == BSub {
				v = -v
			}
			v += k
			switch {
			case v == 0:
				return x.L
			case v > 0:
				return &Binary{Op: BAdd, L: x.L, R: &IntLit{V: v}}
			default:
				return &Binary{Op: BSub, L: x.L, R: &IntLit{V: -v}}
			}
		}
	}
	if k > 0 {
		return &Binary{Op: BAdd, L: e, R: &IntLit{V: k}}
	}
	return &Binary{Op: BSub, L: e, R: &IntLit{V: -k}}
}

// negate returns the logical negation of a condition, simplifying where it
// can so lowered jumps stay readable.
func negate(e Expr) Expr {
	switch x := e.(type) {
	case *BoolLit:
		return &BoolLit{V: !x.V}
	case *Unary:
		if x.Op == UNot {
			return x.X
		}
	case *Binary:
		flip := map[BinOp]BinOp{BEq: BNe, BNe: BEq, BLt: BGe, BGe: BLt, BLe: BGt, BGt: BLe}
		if op, ok := flip[x.Op]; ok {
			return &Binary{Op: op, L: x.L, R: x.R, Line: x.Line}
		}
	}
	return &Unary{Op: UNot, X: e}
}
