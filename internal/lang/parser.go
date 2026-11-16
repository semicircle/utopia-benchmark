package lang

import "fmt"

// Match holds what a shape captured, keyed by slot name.
type Match struct {
	E    map[string]Expr
	I    map[string]string
	B    map[string][]Stmt
	S    map[string]Stmt
	G    map[string][]*Match
	Line int
}

func NewMatch(line int) *Match {
	return &Match{
		E: map[string]Expr{}, I: map[string]string{}, B: map[string][]Stmt{},
		S: map[string]Stmt{}, G: map[string][]*Match{}, Line: line,
	}
}

// BinPrec is the binding power of a binary operator in this dialect.
func (d *Dialect) BinPrec(op BinOp) int {
	if d.Sem.Prec != PrecStandard {
		return 1
	}
	switch op {
	case BOr:
		return 1
	case BAnd:
		return 2
	case BEq, BNe, BLt, BLe, BGt, BGe:
		return 3
	case BAdd, BSub, BConcat:
		return 4
	default:
		return 5
	}
}

func (d *Dialect) RightAssoc() bool { return d.Sem.Prec == PrecFlatRight }

// BinOpText is how a binary operator is spelled in this dialect.
func (d *Dialect) BinOpText(op BinOp) string {
	switch op {
	case BAdd:
		return "+"
	case BSub:
		return "-"
	case BMul:
		return "*"
	case BDiv:
		return "/"
	case BMod:
		if d.Ops.Mod == "" {
			return d.Word(RMod)
		}
		return d.Ops.Mod
	case BConcat:
		return d.Ops.Concat
	case BEq:
		return d.Ops.Eq
	case BNe:
		return d.Ops.Ne
	case BLt:
		return "<"
	case BLe:
		return "<="
	case BGt:
		return ">"
	case BGe:
		return ">="
	case BAnd:
		return d.Word(RAnd)
	case BOr:
		return d.Word(ROr)
	}
	return "?"
}

type parser struct {
	d           *Dialect
	toks        []Token
	pos         int
	kwStarts    map[Role][]Construct
	identStarts []Construct
	binPunct    map[string]BinOp
	binKw       map[Role]BinOp
	builtins    map[string]Builtin
}

func newParser(d *Dialect, toks []Token) *parser {
	p := &parser{d: d, toks: toks, kwStarts: map[Role][]Construct{},
		binPunct: map[string]BinOp{}, binKw: map[Role]BinOp{}, builtins: map[string]Builtin{}}
	for _, c := range ConstructOrder {
		shape, ok := d.Shapes[c]
		if !ok {
			continue
		}
		switch shape[0].Kind {
		case PKw:
			p.kwStarts[shape[0].Role] = append(p.kwStarts[shape[0].Role], c)
		case PIdent:
			p.identStarts = append(p.identStarts, c)
		}
	}
	for _, op := range []BinOp{BAdd, BSub, BMul, BDiv, BConcat, BEq, BNe, BLt, BLe, BGt, BGe} {
		t := d.BinOpText(op)
		if _, dup := p.binPunct[t]; !dup {
			p.binPunct[t] = op
		}
	}
	if d.Ops.Mod == "" {
		p.binKw[RMod] = BMod
	} else {
		p.binPunct[d.Ops.Mod] = BMod
	}
	p.binKw[RAnd] = BAnd
	p.binKw[ROr] = BOr
	for b, w := range d.Builtins {
		p.builtins[w] = b
	}
	return p
}

// Parse parses a whole program in dialect d.
func Parse(d *Dialect, src string) (*Program, error) {
	toks, err := Lex(d, src)
	if err != nil {
		return nil, err
	}
	p := newParser(d, toks)
	prog := &Program{}
	for p.cur().Kind != TEOF {
		if p.startsFunc() {
			m, err := p.matchShape(d.Shapes[CFunc])
			if err != nil {
				return nil, err
			}
			prog.Funcs = append(prog.Funcs, buildFunc(m))
			continue
		}
		if !p.isStmtStart() {
			return nil, p.errf("expected a statement but found %s", describe(p.cur()))
		}
		s, err := p.parseStmt()
		if err != nil {
			return nil, err
		}
		prog.Main = append(prog.Main, s)
	}
	return prog, nil
}

// ParseExpr parses a single expression (used by tests and tools).
func ParseExpr(d *Dialect, src string) (Expr, error) {
	toks, err := Lex(d, src)
	if err != nil {
		return nil, err
	}
	p := newParser(d, toks)
	e, err := p.parseExpr()
	if err != nil {
		return nil, err
	}
	if p.cur().Kind != TEOF {
		return nil, p.errf("unexpected %s after expression", describe(p.cur()))
	}
	return e, nil
}

func (p *parser) cur() Token { return p.toks[p.pos] }
func (p *parser) at(k int) Token {
	if k >= len(p.toks) {
		return p.toks[len(p.toks)-1]
	}
	return p.toks[k]
}
func (p *parser) next() Token {
	t := p.toks[p.pos]
	if t.Kind != TEOF {
		p.pos++
	}
	return t
}

func (p *parser) errf(format string, args ...any) error {
	t := p.cur()
	return &Error{Line: t.Line, Col: t.Col, Msg: fmt.Sprintf(format, args...)}
}

func describe(t Token) string {
	switch t.Kind {
	case TEOF:
		return "end of file"
	case TStr:
		return "a string"
	case TInt:
		return "number " + t.Text
	case TIdent:
		return "name `" + t.Text + "`"
	}
	return "`" + t.Text + "`"
}

func (p *parser) startsFunc() bool {
	shape, ok := p.d.Shapes[CFunc]
	return ok && p.canStartAt(shape, p.pos)
}

func (p *parser) isStmtStart() bool {
	t := p.cur()
	switch t.Kind {
	case TIdent:
		return true
	case TKw:
		return len(p.kwStarts[t.Role]) > 0 && !(p.startsFunc())
	}
	return false
}

func (p *parser) parseStmt() (Stmt, error) {
	t := p.cur()
	var cands []Construct
	if t.Kind == TIdent {
		cands = p.identStarts
	} else if t.Kind == TKw {
		cands = p.kwStarts[t.Role]
	}
	for _, c := range cands {
		if c == CFunc {
			continue
		}
		shape := p.d.Shapes[c]
		if p.canStartAt(shape, p.pos) {
			m, err := p.matchShape(shape)
			if err != nil {
				return nil, err
			}
			s := buildStmt(c, m)
			if cs, ok := s.(*CallStmt); ok {
				cs.Call.Builtin = p.builtins[cs.Call.Name]
			}
			return s, nil
		}
	}
	if t.Kind == TIdent {
		nt := p.at(p.pos + 1)
		return nil, &Error{nt.Line, nt.Col, fmt.Sprintf("unexpected %s after `%s` (expected assignment `%s`, a call, or an index)", describe(nt), t.Text, p.d.Ops.Assign)}
	}
	return nil, p.errf("%s cannot start a statement here", describe(t))
}

func (p *parser) parseBody() ([]Stmt, error) {
	var out []Stmt
	for {
		if p.startsFunc() {
			return nil, p.errf("functions can only be declared at the top level, not inside a block")
		}
		if !p.isStmtStart() {
			return out, nil
		}
		s, err := p.parseStmt()
		if err != nil {
			return nil, err
		}
		out = append(out, s)
	}
}

func (p *parser) isTerm(t Token) bool { return t.Kind == TPunct && t.Text == p.d.Terminator }

// canStartAt reports whether parts could begin at token index k, looking
// ahead through leading keywords, punctuation and identifiers.
func (p *parser) canStartAt(parts []Part, k int) bool {
	for _, part := range parts {
		t := p.at(k)
		switch part.Kind {
		case PKw:
			if t.Kind != TKw || t.Role != part.Role {
				return false
			}
		case PPunct:
			if t.Kind != TPunct || t.Text != part.Text {
				return false
			}
		case PTerm:
			if !p.isTerm(t) {
				return false
			}
		case PIdent, PSame:
			if t.Kind != TIdent {
				return false
			}
		case PExpr:
			return p.canStartExpr(t)
		case PLit:
			return isLitStart(t)
		case POpt, PRep:
			return true
		case PList:
			if part.Min == 0 {
				return true
			}
			return p.canStartAt(part.Sub, k)
		default:
			return true
		}
		k++
	}
	return true
}

func isLitStart(t Token) bool {
	return t.Kind == TInt || t.Kind == TStr || (t.Kind == TPunct && t.Text == "-")
}

func (p *parser) canStartExpr(t Token) bool {
	switch t.Kind {
	case TInt, TStr, TIdent:
		return true
	case TPunct:
		return t.Text == "(" || t.Text == "[" || t.Text == "-"
	case TKw:
		return t.Role == RTrue || t.Role == RFalse || t.Role == RNone || t.Role == RNot
	}
	return false
}

func (p *parser) matchShape(parts []Part) (*Match, error) {
	m := NewMatch(p.cur().Line)
	return m, p.matchParts(parts, m)
}

func (p *parser) expectText(t Token, want string) error {
	return &Error{t.Line, t.Col, fmt.Sprintf("expected `%s` but found %s", want, describe(t))}
}

func (p *parser) matchParts(parts []Part, m *Match) error {
	for _, part := range parts {
		t := p.cur()
		switch part.Kind {
		case PKw:
			if t.Kind != TKw || t.Role != part.Role {
				return p.expectText(t, p.d.Word(part.Role))
			}
			p.next()
		case PPunct:
			if t.Kind != TPunct || t.Text != part.Text {
				return p.expectText(t, part.Text)
			}
			p.next()
		case PTerm:
			if !p.isTerm(t) {
				return p.expectText(t, p.d.Terminator)
			}
			p.next()
		case PExpr:
			e, err := p.parseExpr()
			if err != nil {
				return err
			}
			m.E[part.Slot] = e
		case PIdent:
			if t.Kind == TKw {
				return p.errf("`%s` is a keyword and cannot be used as a name", t.Text)
			}
			if t.Kind != TIdent {
				return p.errf("expected a name but found %s", describe(t))
			}
			m.I[part.Slot] = t.Text
			p.next()
		case PSame:
			want := m.I[part.Slot]
			if t.Kind != TIdent || t.Text != want {
				return p.expectText(t, want)
			}
			p.next()
		case PBody:
			b, err := p.parseBody()
			if err != nil {
				return err
			}
			m.B[part.Slot] = b
		case PSimple:
			if t.Kind == TIdent || (t.Kind == TKw && t.Role == RLet) {
				s, err := p.parseSimple()
				if err != nil {
					return err
				}
				m.S[part.Slot] = s
			}
		case PLit:
			e, err := p.parseLit()
			if err != nil {
				return err
			}
			m.E[part.Slot] = e
		case POpt:
			if p.canStartAt(part.Sub, p.pos) {
				g := NewMatch(t.Line)
				if err := p.matchParts(part.Sub, g); err != nil {
					return err
				}
				m.G[part.Slot] = []*Match{g}
			}
		case PRep:
			for p.canStartAt(part.Sub, p.pos) {
				g := NewMatch(p.cur().Line)
				if err := p.matchParts(part.Sub, g); err != nil {
					return err
				}
				m.G[part.Slot] = append(m.G[part.Slot], g)
			}
		case PList:
			if part.Min == 0 && !p.canStartAt(part.Sub, p.pos) {
				continue
			}
			for {
				g := NewMatch(p.cur().Line)
				if err := p.matchParts(part.Sub, g); err != nil {
					return err
				}
				m.G[part.Slot] = append(m.G[part.Slot], g)
				if c := p.cur(); c.Kind == TPunct && c.Text == part.Text {
					p.next()
					continue
				}
				break
			}
		}
	}
	return nil
}

// SimpleShape returns the shape of a let/assign statement without its
// terminator, as used in the header of a C-style for loop.
func SimpleShape(d *Dialect, c Construct) []Part {
	s := d.Shapes[c]
	if len(s) > 0 && s[len(s)-1].Kind == PTerm {
		return s[:len(s)-1]
	}
	return s
}

func (p *parser) parseSimple() (Stmt, error) {
	for _, c := range []Construct{CLet, CIndexAssign, CAssign} {
		shape := SimpleShape(p.d, c)
		if p.canStartAt(shape, p.pos) {
			m, err := p.matchShape(shape)
			if err != nil {
				return nil, err
			}
			return buildStmt(c, m), nil
		}
	}
	return nil, p.errf("expected an assignment but found %s", describe(p.cur()))
}

func (p *parser) parseLit() (Expr, error) {
	t := p.cur()
	switch {
	case t.Kind == TInt:
		p.next()
		return &IntLit{V: t.Int}, nil
	case t.Kind == TStr:
		p.next()
		return &StrLit{V: t.Text}, nil
	case t.Kind == TPunct && t.Text == "-" && p.at(p.pos+1).Kind == TInt:
		p.next()
		n := p.next()
		return &IntLit{V: -n.Int}, nil
	}
	return nil, p.errf("expected a number or string literal but found %s", describe(t))
}

// ---- expressions ----

func (p *parser) parseExpr() (Expr, error) { return p.parseBin(0) }

func (p *parser) peekBinop() (BinOp, bool) {
	t := p.cur()
	if t.Kind == TPunct {
		op, ok := p.binPunct[t.Text]
		return op, ok
	}
	if t.Kind == TKw {
		op, ok := p.binKw[t.Role]
		return op, ok
	}
	return 0, false
}

func (p *parser) parseBin(minPrec int) (Expr, error) {
	left, err := p.parseUnary()
	if err != nil {
		return nil, err
	}
	for {
		op, ok := p.peekBinop()
		if !ok {
			return left, nil
		}
		pr := p.d.BinPrec(op)
		if pr < minPrec {
			return left, nil
		}
		line := p.next().Line
		next := pr + 1
		if p.d.RightAssoc() {
			next = pr
		}
		right, err := p.parseBin(next)
		if err != nil {
			return nil, err
		}
		left = &Binary{Op: op, L: left, R: right, Line: line}
	}
}

func (p *parser) parseUnary() (Expr, error) {
	t := p.cur()
	if t.Kind == TPunct && t.Text == "-" {
		p.next()
		x, err := p.parseUnary()
		if err != nil {
			return nil, err
		}
		return &Unary{Op: UNeg, X: x}, nil
	}
	if t.Kind == TKw && t.Role == RNot {
		p.next()
		x, err := p.parseUnary()
		if err != nil {
			return nil, err
		}
		return &Unary{Op: UNot, X: x}, nil
	}
	x, err := p.parsePrimary()
	if err != nil {
		return nil, err
	}
	for p.cur().Kind == TPunct && p.cur().Text == "[" {
		line := p.next().Line
		i, err := p.parseExpr()
		if err != nil {
			return nil, err
		}
		if c := p.cur(); c.Kind != TPunct || c.Text != "]" {
			return nil, p.expectText(c, "]")
		}
		p.next()
		x = &Index{X: x, I: i, Line: line}
	}
	return x, nil
}

func (p *parser) parsePrimary() (Expr, error) {
	t := p.cur()
	switch t.Kind {
	case TInt:
		p.next()
		return &IntLit{V: t.Int}, nil
	case TStr:
		p.next()
		return &StrLit{V: t.Text}, nil
	case TKw:
		switch t.Role {
		case RTrue:
			p.next()
			return &BoolLit{V: true}, nil
		case RFalse:
			p.next()
			return &BoolLit{V: false}, nil
		case RNone:
			p.next()
			return &NoneLit{}, nil
		}
		return nil, p.errf("keyword `%s` cannot be used inside an expression", t.Text)
	case TIdent:
		p.next()
		if c := p.cur(); c.Kind == TPunct && c.Text == "(" {
			p.next()
			args, err := p.parseExprList(")")
			if err != nil {
				return nil, err
			}
			return &Call{Name: t.Text, Builtin: p.builtins[t.Text], Args: args, Line: t.Line}, nil
		}
		return &Ident{Name: t.Text, Line: t.Line}, nil
	case TPunct:
		switch t.Text {
		case "(":
			p.next()
			e, err := p.parseExpr()
			if err != nil {
				return nil, err
			}
			if c := p.cur(); c.Kind != TPunct || c.Text != ")" {
				return nil, p.expectText(c, ")")
			}
			p.next()
			return e, nil
		case "[":
			p.next()
			elems, err := p.parseExprList("]")
			if err != nil {
				return nil, err
			}
			return &ListLit{Elems: elems}, nil
		}
	}
	return nil, p.errf("expected an expression but found %s", describe(t))
}

// parseExprList parses comma-separated expressions up to and including close.
func (p *parser) parseExprList(close string) ([]Expr, error) {
	var out []Expr
	if c := p.cur(); c.Kind == TPunct && c.Text == close {
		p.next()
		return out, nil
	}
	for {
		e, err := p.parseExpr()
		if err != nil {
			return nil, err
		}
		out = append(out, e)
		c := p.cur()
		if c.Kind == TPunct && c.Text == "," {
			p.next()
			continue
		}
		if c.Kind == TPunct && c.Text == close {
			p.next()
			return out, nil
		}
		return nil, p.errf("expected `,` or `%s` but found %s", close, describe(c))
	}
}
