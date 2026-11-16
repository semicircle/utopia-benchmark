// Package vm compiles a parsed program to bytecode and runs it
// deterministically. All dialect semantics (evaluation order, division,
// indexing, ...) are applied here.
package vm

import (
	"fmt"

	. "utopia/internal/lang"
)

type Op uint8

const (
	OpConst Op = iota
	OpNone
	OpLoad
	OpStore
	OpPop
	OpSwap
	OpAdd
	OpSub
	OpMul
	OpDiv
	OpMod
	OpConcat
	OpEq
	OpNe
	OpLt
	OpLe
	OpGt
	OpGe
	OpAnd
	OpOr
	OpNot
	OpNeg
	OpCheckBool
	OpJump
	OpJumpIfFalse     // pops a bool
	OpJumpIfTrue      // pops a bool
	OpJumpIfFalseKeep // peeks a bool (short-circuit and)
	OpJumpIfTrueKeep  // peeks a bool (short-circuit or)
	OpCall            // A = function, B = argc, C = 1 if args were pushed right to left
	OpBuiltin         // A = builtin, B = argc, C = 1 if reversed
	OpRet
	OpHalt
	OpPrint // A = 1 for newline
	OpList  // A = count
	OpIndex
	OpSetIndex
	OpCheckStep
	OpForCond // A = 1 if inclusive; pops step, limit, value
)

type Instr struct {
	Op      Op
	A, B, C int32
	Line    int32
}

type Func struct {
	Name    string
	NParams int
	NLocals int
	Code    []Instr
	Locals  []string
}

type Module struct {
	Funcs  []*Func
	Consts []Value
	Main   int
}

type loopCtx struct {
	isSwitch  bool
	breaks    []int
	continues []int
}

type compiler struct {
	d       *Dialect
	mod     *Module
	funcIdx map[string]int
	decls   map[string]*FuncDecl

	fn       *Func
	locals   map[string]int
	ctx      []*loopCtx
	labels   map[string]int
	gotoFix  []gotoFix
	tmpCount int
	line     int
}

type gotoFix struct {
	at    int
	label string
	line  int
}

// Compile turns a program into a module for dialect d.
func Compile(d *Dialect, prog *Program) (*Module, error) {
	c := &compiler{d: d, mod: &Module{}, funcIdx: map[string]int{}, decls: map[string]*FuncDecl{}}
	builtinNames := map[string]bool{}
	for _, w := range d.Builtins {
		builtinNames[w] = true
	}
	for _, f := range prog.Funcs {
		if builtinNames[f.Name] {
			return nil, &Error{Line: f.Line, Msg: fmt.Sprintf("`%s` is a builtin and cannot be redefined", f.Name)}
		}
		if _, dup := c.funcIdx[f.Name]; dup {
			return nil, &Error{Line: f.Line, Msg: fmt.Sprintf("function `%s` is declared twice", f.Name)}
		}
		seen := map[string]bool{}
		for _, p := range f.Params {
			if seen[p] {
				return nil, &Error{Line: f.Line, Msg: fmt.Sprintf("parameter `%s` appears twice", p)}
			}
			seen[p] = true
		}
		c.funcIdx[f.Name] = len(c.mod.Funcs)
		c.decls[f.Name] = f
		c.mod.Funcs = append(c.mod.Funcs, &Func{Name: f.Name, NParams: len(f.Params)})
	}
	for _, f := range prog.Funcs {
		if err := c.compileFunc(c.mod.Funcs[c.funcIdx[f.Name]], f.Params, f.Body, false); err != nil {
			return nil, err
		}
	}
	main := &Func{Name: "<main>"}
	c.mod.Main = len(c.mod.Funcs)
	c.mod.Funcs = append(c.mod.Funcs, main)
	if err := c.compileFunc(main, nil, prog.Main, true); err != nil {
		return nil, err
	}
	return c.mod, nil
}

func (c *compiler) compileFunc(fn *Func, params []string, body []Stmt, isMain bool) error {
	c.fn = fn
	c.locals = map[string]int{}
	c.labels = map[string]int{}
	c.gotoFix = nil
	c.ctx = nil
	for _, p := range params {
		c.declare(p)
	}
	if err := c.block(body); err != nil {
		return err
	}
	if isMain {
		c.emit(OpHalt, 0, 0, 0)
	} else {
		c.emit(OpNone, 0, 0, 0)
		c.emit(OpRet, 0, 0, 0)
	}
	for _, g := range c.gotoFix {
		target, ok := c.labels[g.label]
		if !ok {
			return &Error{Line: g.line, Msg: fmt.Sprintf("label `%s` is not defined in this function", g.label)}
		}
		fn.Code[g.at].A = int32(target)
	}
	fn.NLocals = len(fn.Locals)
	return nil
}

func (c *compiler) declare(name string) int {
	if i, ok := c.locals[name]; ok {
		return i
	}
	i := len(c.fn.Locals)
	c.fn.Locals = append(c.fn.Locals, name)
	c.locals[name] = i
	return i
}

func (c *compiler) temp() int {
	c.tmpCount++
	return c.declare(fmt.Sprintf(" t%d", c.tmpCount)) // space: cannot clash with user names
}

func (c *compiler) emit(op Op, a, b, cc int) int {
	c.fn.Code = append(c.fn.Code, Instr{Op: op, A: int32(a), B: int32(b), C: int32(cc), Line: int32(c.line)})
	return len(c.fn.Code) - 1
}

func (c *compiler) here() int        { return len(c.fn.Code) }
func (c *compiler) patch(at, to int) { c.fn.Code[at].A = int32(to) }

func (c *compiler) constant(v Value) int {
	c.mod.Consts = append(c.mod.Consts, v)
	return len(c.mod.Consts) - 1
}

func (c *compiler) errf(line int, format string, args ...any) error {
	return &Error{Line: line, Msg: fmt.Sprintf(format, args...)}
}

func (c *compiler) block(stmts []Stmt) error {
	for _, s := range stmts {
		if err := c.stmt(s); err != nil {
			return err
		}
	}
	return nil
}

func (c *compiler) setLine(l int) {
	if l > 0 {
		c.line = l
	}
}

func (c *compiler) stmt(s Stmt) error {
	switch s := s.(type) {
	case *Let:
		c.setLine(s.Line)
		if err := c.expr(s.Value); err != nil {
			return err
		}
		c.emit(OpStore, c.declare(s.Name), 0, 0)
	case *Assign:
		c.setLine(s.Line)
		slot, ok := c.locals[s.Name]
		if !ok {
			return c.errf(s.Line, "variable `%s` is not declared; declare it first with `%s`", s.Name, c.d.Word(RLet))
		}
		if err := c.expr(s.Value); err != nil {
			return err
		}
		c.emit(OpStore, slot, 0, 0)
	case *IndexAssign:
		c.setLine(s.Line)
		slot, ok := c.locals[s.Name]
		if !ok {
			return c.errf(s.Line, "variable `%s` is not declared", s.Name)
		}
		c.emit(OpLoad, slot, 0, 0)
		if err := c.expr(s.Index); err != nil {
			return err
		}
		if err := c.expr(s.Value); err != nil {
			return err
		}
		c.emit(OpSetIndex, 0, 0, 0)
	case *CallStmt:
		c.setLine(s.Call.Line)
		if err := c.expr(s.Call); err != nil {
			return err
		}
		c.emit(OpPop, 0, 0, 0)
	case *Print:
		c.setLine(s.Line)
		if err := c.expr(s.Value); err != nil {
			return err
		}
		nl := 0
		if s.Newline {
			nl = 1
		}
		c.emit(OpPrint, nl, 0, 0)
	case *Return:
		c.setLine(s.Line)
		if s.Value != nil {
			if err := c.expr(s.Value); err != nil {
				return err
			}
		} else {
			c.emit(OpNone, 0, 0, 0)
		}
		if c.fn == c.mod.Funcs[len(c.mod.Funcs)-1] && c.fn.Name == "<main>" {
			c.emit(OpHalt, 0, 0, 0)
		} else {
			c.emit(OpRet, 0, 0, 0)
		}
	case *Break:
		c.setLine(s.Line)
		if len(c.ctx) == 0 {
			return c.errf(s.Line, "`%s` used outside a loop", c.d.Word(RBreak))
		}
		lc := c.ctx[len(c.ctx)-1]
		lc.breaks = append(lc.breaks, c.emit(OpJump, 0, 0, 0))
	case *Continue:
		c.setLine(s.Line)
		var lc *loopCtx
		for i := len(c.ctx) - 1; i >= 0; i-- {
			if !c.ctx[i].isSwitch {
				lc = c.ctx[i]
				break
			}
		}
		if lc == nil {
			return c.errf(s.Line, "`%s` used outside a loop", c.d.Word(RContinue))
		}
		lc.continues = append(lc.continues, c.emit(OpJump, 0, 0, 0))
	case *Label:
		c.setLine(s.Line)
		if _, dup := c.labels[s.Name]; dup {
			return c.errf(s.Line, "label `%s` is defined twice", s.Name)
		}
		c.labels[s.Name] = c.here()
	case *Goto:
		c.setLine(s.Line)
		c.gotoFix = append(c.gotoFix, gotoFix{c.emit(OpJump, 0, 0, 0), s.Label, s.Line})
	case *JumpIf:
		c.setLine(s.Line)
		if err := c.expr(s.Cond); err != nil {
			return err
		}
		c.gotoFix = append(c.gotoFix, gotoFix{c.emit(OpJumpIfTrue, 0, 0, 0), s.Label, s.Line})
	case *If:
		c.setLine(s.Line)
		var ends []int
		for _, arm := range s.Arms {
			if err := c.expr(arm.Cond); err != nil {
				return err
			}
			skip := c.emit(OpJumpIfFalse, 0, 0, 0)
			if err := c.block(arm.Body); err != nil {
				return err
			}
			ends = append(ends, c.emit(OpJump, 0, 0, 0))
			c.patch(skip, c.here())
		}
		if s.HasElse {
			if err := c.block(s.Else); err != nil {
				return err
			}
		}
		for _, e := range ends {
			c.patch(e, c.here())
		}
	case *Switch:
		return c.switchStmt(s)
	case *Dispatch:
		c.setLine(s.Line)
		if err := c.expr(s.Subject); err != nil {
			return err
		}
		tmp := c.temp()
		c.emit(OpStore, tmp, 0, 0)
		seen := map[string]bool{}
		for _, e := range s.Entries {
			key := litKey(e.Value)
			if seen[key] {
				return c.errf(s.Line, "value %s appears twice", key)
			}
			seen[key] = true
			c.emit(OpLoad, tmp, 0, 0)
			c.emit(OpConst, c.constant(litValue(e.Value)), 0, 0)
			c.emit(OpEq, 0, 0, 0)
			c.gotoFix = append(c.gotoFix, gotoFix{c.emit(OpJumpIfTrue, 0, 0, 0), e.Label, s.Line})
		}
		if s.Else != "" {
			c.gotoFix = append(c.gotoFix, gotoFix{c.emit(OpJump, 0, 0, 0), s.Else, s.Line})
		}
	case *While:
		c.setLine(s.Line)
		top := c.here()
		if err := c.expr(s.Cond); err != nil {
			return err
		}
		exit := c.emit(OpJumpIfFalse, 0, 0, 0)
		lc, err := c.loopBody(s.Body)
		if err != nil {
			return err
		}
		c.emit(OpJump, top, 0, 0)
		c.closeLoop(lc, top, c.here())
		c.patch(exit, c.here())
	case *DoWhile:
		c.setLine(s.Line)
		top := c.here()
		lc, err := c.loopBody(s.Body)
		if err != nil {
			return err
		}
		cont := c.here()
		if err := c.expr(s.Cond); err != nil {
			return err
		}
		c.emit(OpJumpIfTrue, top, 0, 0)
		c.closeLoop(lc, cont, c.here())
	case *RepeatUntil:
		c.setLine(s.Line)
		top := c.here()
		lc, err := c.loopBody(s.Body)
		if err != nil {
			return err
		}
		cont := c.here()
		if err := c.expr(s.Cond); err != nil {
			return err
		}
		c.emit(OpJumpIfFalse, top, 0, 0)
		c.closeLoop(lc, cont, c.here())
	case *CFor:
		c.setLine(s.Line)
		if s.Init != nil {
			if err := c.stmt(s.Init); err != nil {
				return err
			}
		}
		top := c.here()
		if err := c.expr(s.Cond); err != nil {
			return err
		}
		exit := c.emit(OpJumpIfFalse, 0, 0, 0)
		lc, err := c.loopBody(s.Body)
		if err != nil {
			return err
		}
		cont := c.here()
		if s.Post != nil {
			if err := c.stmt(s.Post); err != nil {
				return err
			}
		}
		c.emit(OpJump, top, 0, 0)
		c.closeLoop(lc, cont, c.here())
		c.patch(exit, c.here())
	case *CountFor:
		c.setLine(s.Line)
		if err := c.expr(s.From); err != nil {
			return err
		}
		v := c.declare(s.Var)
		c.emit(OpStore, v, 0, 0)
		if err := c.expr(s.To); err != nil {
			return err
		}
		limit := c.temp()
		c.emit(OpStore, limit, 0, 0)
		if s.Step != nil {
			if err := c.expr(s.Step); err != nil {
				return err
			}
		} else {
			c.emit(OpConst, c.constant(IntVal(1)), 0, 0)
		}
		c.emit(OpCheckStep, 0, 0, 0)
		step := c.temp()
		c.emit(OpStore, step, 0, 0)
		top := c.here()
		c.emit(OpLoad, v, 0, 0)
		c.emit(OpLoad, limit, 0, 0)
		c.emit(OpLoad, step, 0, 0)
		incl := 0
		if c.d.Sem.CountInclusive {
			incl = 1
		}
		c.emit(OpForCond, incl, 0, 0)
		exit := c.emit(OpJumpIfFalse, 0, 0, 0)
		lc, err := c.loopBody(s.Body)
		if err != nil {
			return err
		}
		cont := c.here()
		c.emit(OpLoad, v, 0, 0)
		c.emit(OpLoad, step, 0, 0)
		c.emit(OpAdd, 0, 0, 0)
		c.emit(OpStore, v, 0, 0)
		c.emit(OpJump, top, 0, 0)
		c.closeLoop(lc, cont, c.here())
		c.patch(exit, c.here())
	default:
		return fmt.Errorf("compile: unknown statement %T", s)
	}
	return nil
}

func (c *compiler) loopBody(body []Stmt) (*loopCtx, error) {
	lc := &loopCtx{}
	c.ctx = append(c.ctx, lc)
	err := c.block(body)
	c.ctx = c.ctx[:len(c.ctx)-1]
	return lc, err
}

func (c *compiler) closeLoop(lc *loopCtx, cont, end int) {
	for _, b := range lc.breaks {
		c.patch(b, end)
	}
	for _, k := range lc.continues {
		c.patch(k, cont)
	}
}

// switchIsBreakTarget: in C-style switches `break` leaves the switch; in the
// other styles it refers to the enclosing loop.
func (c *compiler) switchIsBreakTarget() bool {
	return c.d.Styles.Switch == StyleC || c.d.Styles.Switch == StyleCanon
}

func (c *compiler) switchStmt(s *Switch) error {
	c.setLine(s.Line)
	if err := c.expr(s.Subject); err != nil {
		return err
	}
	tmp := c.temp()
	c.emit(OpStore, tmp, 0, 0)
	seen := map[string]bool{}
	jumps := make([][]int, len(s.Cases))
	for i, cs := range s.Cases {
		for _, v := range cs.Values {
			key := litKey(v)
			if seen[key] {
				return c.errf(s.Line, "case value %s appears twice", key)
			}
			seen[key] = true
			c.emit(OpLoad, tmp, 0, 0)
			c.emit(OpConst, c.constant(litValue(v)), 0, 0)
			c.emit(OpEq, 0, 0, 0)
			jumps[i] = append(jumps[i], c.emit(OpJumpIfTrue, 0, 0, 0))
		}
	}
	toDefault := c.emit(OpJump, 0, 0, 0)
	lc := &loopCtx{isSwitch: true}
	if c.switchIsBreakTarget() {
		c.ctx = append(c.ctx, lc)
	}
	fall := c.d.Sem.SwitchFallthrough && c.switchIsBreakTarget() && c.d.Styles.Switch == StyleC
	var ends []int
	for i, cs := range s.Cases {
		for _, j := range jumps[i] {
			c.patch(j, c.here())
		}
		if err := c.block(cs.Body); err != nil {
			return err
		}
		if !fall {
			ends = append(ends, c.emit(OpJump, 0, 0, 0))
		}
	}
	c.patch(toDefault, c.here())
	if s.HasDefault {
		if err := c.block(s.Default); err != nil {
			return err
		}
	}
	if c.switchIsBreakTarget() {
		c.ctx = c.ctx[:len(c.ctx)-1]
	}
	for _, e := range ends {
		c.patch(e, c.here())
	}
	for _, b := range lc.breaks {
		c.patch(b, c.here())
	}
	return nil
}

func litValue(e Expr) Value {
	switch e := e.(type) {
	case *IntLit:
		return IntVal(e.V)
	case *StrLit:
		return StrVal(e.V)
	case *Unary:
		if l, ok := e.X.(*IntLit); ok && e.Op == UNeg {
			return IntVal(-l.V)
		}
	}
	return NoneVal()
}

func litKey(e Expr) string {
	v := litValue(e)
	if v.K == KStr {
		return QuoteString(v.S)
	}
	return fmt.Sprint(v.I)
}

func (c *compiler) exprs(es []Expr, reversed bool) error {
	for i := range es {
		k := i
		if reversed {
			k = len(es) - 1 - i
		}
		if err := c.expr(es[k]); err != nil {
			return err
		}
	}
	return nil
}

func (c *compiler) expr(e Expr) error {
	switch e := e.(type) {
	case *IntLit:
		c.emit(OpConst, c.constant(IntVal(e.V)), 0, 0)
	case *StrLit:
		c.emit(OpConst, c.constant(StrVal(e.V)), 0, 0)
	case *BoolLit:
		c.emit(OpConst, c.constant(BoolVal(e.V)), 0, 0)
	case *NoneLit:
		c.emit(OpNone, 0, 0, 0)
	case *ListLit:
		if err := c.exprs(e.Elems, false); err != nil {
			return err
		}
		c.emit(OpList, len(e.Elems), 0, 0)
	case *Ident:
		c.setLine(e.Line)
		slot, ok := c.locals[e.Name]
		if !ok {
			if _, isFn := c.funcIdx[e.Name]; isFn {
				return c.errf(e.Line, "`%s` is a function; call it with parentheses", e.Name)
			}
			return c.errf(e.Line, "unknown variable `%s`", e.Name)
		}
		c.emit(OpLoad, slot, 0, 0)
	case *Unary:
		if err := c.expr(e.X); err != nil {
			return err
		}
		if e.Op == UNeg {
			c.emit(OpNeg, 0, 0, 0)
		} else {
			c.emit(OpNot, 0, 0, 0)
		}
	case *Index:
		c.setLine(e.Line)
		if err := c.expr(e.X); err != nil {
			return err
		}
		if err := c.expr(e.I); err != nil {
			return err
		}
		c.emit(OpIndex, 0, 0, 0)
	case *Call:
		c.setLine(e.Line)
		rev := c.d.Sem.ArgOrder == RightToLeft
		revFlag := 0
		if rev {
			revFlag = 1
		}
		if e.Builtin != BNone {
			if n := BuiltinArity[e.Builtin]; n != len(e.Args) {
				return c.errf(e.Line, "`%s` takes %d argument(s), got %d", e.Name, n, len(e.Args))
			}
			if err := c.exprs(e.Args, rev); err != nil {
				return err
			}
			c.emit(OpBuiltin, int(e.Builtin), len(e.Args), revFlag)
			return nil
		}
		idx, ok := c.funcIdx[e.Name]
		if !ok {
			return c.errf(e.Line, "unknown function `%s`", e.Name)
		}
		if n := len(c.decls[e.Name].Params); n != len(e.Args) {
			return c.errf(e.Line, "`%s` takes %d argument(s), got %d", e.Name, n, len(e.Args))
		}
		if err := c.exprs(e.Args, rev); err != nil {
			return err
		}
		c.setLine(e.Line)
		c.emit(OpCall, idx, len(e.Args), revFlag)
	case *Binary:
		c.setLine(e.Line)
		if (e.Op == BAnd || e.Op == BOr) && c.d.Sem.ShortCircuit {
			if err := c.expr(e.L); err != nil {
				return err
			}
			op := OpJumpIfFalseKeep
			if e.Op == BOr {
				op = OpJumpIfTrueKeep
			}
			j := c.emit(op, 0, 0, 0)
			c.emit(OpPop, 0, 0, 0)
			if err := c.expr(e.R); err != nil {
				return err
			}
			c.emit(OpCheckBool, 0, 0, 0)
			c.patch(j, c.here())
			return nil
		}
		if c.d.Sem.OperandOrder == RightToLeft {
			if err := c.expr(e.R); err != nil {
				return err
			}
			if err := c.expr(e.L); err != nil {
				return err
			}
			c.setLine(e.Line)
			c.emit(OpSwap, 0, 0, 0)
		} else {
			if err := c.expr(e.L); err != nil {
				return err
			}
			if err := c.expr(e.R); err != nil {
				return err
			}
		}
		c.setLine(e.Line)
		c.emit(binOps[e.Op], 0, 0, 0)
	default:
		return fmt.Errorf("compile: unknown expression %T", e)
	}
	return nil
}

var binOps = map[BinOp]Op{
	BAdd: OpAdd, BSub: OpSub, BMul: OpMul, BDiv: OpDiv, BMod: OpMod, BConcat: OpConcat,
	BEq: OpEq, BNe: OpNe, BLt: OpLt, BLe: OpLe, BGt: OpGt, BGe: OpGe, BAnd: OpAnd, BOr: OpOr,
}
