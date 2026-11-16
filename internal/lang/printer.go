package lang

import (
	"strconv"
	"strings"
)

// writer lays out tokens with conventional spacing and indentation.
type writer struct {
	sb        strings.Builder
	indent    int
	needNL    bool
	lineStart bool
	glue      bool // next token attaches without a space
	noSpace   bool // previous token wants no space after it
	term      string
}

func newWriter(term string) *writer { return &writer{lineStart: true, term: term} }

func (w *writer) newline() { w.needNL = true }

func (w *writer) blankLine() {
	if w.sb.Len() > 0 {
		w.sb.WriteString("\n")
	}
	w.needNL = true
}

func (w *writer) tok(t string) {
	if w.needNL && w.sb.Len() > 0 {
		w.sb.WriteString("\n")
		w.lineStart = true
	}
	w.needNL = false
	if w.lineStart {
		w.sb.WriteString(strings.Repeat("    ", w.indent))
	} else if !w.glue && !w.noSpace && !noSpaceBefore(t, w.term) {
		w.sb.WriteByte(' ')
	}
	w.sb.WriteString(t)
	w.lineStart, w.glue = false, false
	w.noSpace = t == "(" || t == "["
}

func noSpaceBefore(t, term string) bool {
	switch t {
	case ")", "]", ",", ":", ";":
		return true
	}
	return t == term
}

// unaryMinus writes a minus that binds to the following token.
func (w *writer) unaryMinus() {
	w.tok("-")
	w.noSpace = true
}

func (w *writer) String() string {
	s := w.sb.String()
	if !strings.HasSuffix(s, "\n") {
		s += "\n"
	}
	return s
}

type printer struct {
	d *Dialect
	w *writer
}

// Format renders a program in dialect d.
func Format(d *Dialect, prog *Program) string {
	p := &printer{d: d, w: newWriter(d.Terminator)}
	for i, f := range prog.Funcs {
		if i > 0 {
			p.w.blankLine()
		}
		p.w.newline()
		p.parts(d.Shapes[CFunc], ExtractFunc(f))
	}
	if len(prog.Funcs) > 0 && len(prog.Main) > 0 {
		p.w.blankLine()
	}
	for _, s := range prog.Main {
		p.stmt(s)
	}
	return p.w.String()
}

// FormatExpr renders one expression in dialect d.
func FormatExpr(d *Dialect, e Expr) string {
	p := &printer{d: d, w: newWriter(d.Terminator)}
	p.expr(e)
	return strings.TrimSuffix(p.w.String(), "\n")
}

func (p *printer) stmt(s Stmt) {
	c, m := Extract(s)
	if cs, ok := s.(*CallStmt); ok && cs.Call.Builtin != BNone {
		m.I["fn"] = p.d.Builtins[cs.Call.Builtin]
	}
	shape, ok := p.d.Shapes[c]
	if !ok {
		panic("print: dialect has no syntax for " + string(c) + " (lower the program first)")
	}
	p.w.newline()
	// Labels sit one level left of the statements around them.
	if _, isLabel := s.(*Label); isLabel && p.w.indent > 0 {
		p.w.indent--
		defer func() { p.w.indent++ }()
	}
	p.parts(shape, m)
}

func (p *printer) simple(s Stmt) {
	c, m := Extract(s)
	p.parts(SimpleShape(p.d, c), m)
}

func (p *printer) parts(parts []Part, m *Match) {
	prevKind := PartKind(255)
	for _, part := range parts {
		k := part.Kind
		switch part.Kind {
		case PKw:
			p.w.tok(p.d.Word(part.Role))
		case PPunct:
			// Calls, function headers and indexing glue their bracket to the
			// preceding name.
			if (part.Text == "(" || part.Text == "[") && (prevKind == PIdent || prevKind == PSame) {
				p.w.glue = true
			}
			p.w.tok(part.Text)
		case PTerm:
			p.w.tok(p.d.Terminator)
		case PExpr, PLit:
			p.expr(m.E[part.Slot])
		case PIdent:
			p.w.tok(m.I[part.Slot])
		case PSame:
			p.w.tok(m.I[part.Slot])
		case PBody:
			p.w.indent++
			for _, s := range m.B[part.Slot] {
				p.stmt(s)
			}
			p.w.indent--
			p.w.newline()
		case PSimple:
			if s := m.S[part.Slot]; s != nil {
				p.simple(s)
			}
		case POpt, PRep:
			for _, g := range m.G[part.Slot] {
				if part.NL {
					p.w.newline()
				}
				p.parts(part.Sub, g)
			}
		case PList:
			for i, g := range m.G[part.Slot] {
				if i > 0 {
					p.w.tok(part.Text)
				}
				p.parts(part.Sub, g)
			}
		}
		prevKind = k
	}
}

func (p *printer) expr(e Expr) {
	switch e := e.(type) {
	case *IntLit:
		if e.V < 0 {
			p.w.unaryMinus()
			p.w.tok(strconv.FormatUint(uint64(-e.V), 10))
		} else {
			p.w.tok(strconv.FormatInt(e.V, 10))
		}
	case *StrLit:
		p.w.tok(QuoteString(e.V))
	case *BoolLit:
		if e.V {
			p.w.tok(p.d.Word(RTrue))
		} else {
			p.w.tok(p.d.Word(RFalse))
		}
	case *NoneLit:
		p.w.tok(p.d.Word(RNone))
	case *ListLit:
		p.w.tok("[")
		for i, x := range e.Elems {
			if i > 0 {
				p.w.tok(",")
			}
			p.expr(x)
		}
		p.w.tok("]")
	case *Ident:
		p.w.tok(e.Name)
	case *Call:
		name := e.Name
		if e.Builtin != BNone {
			name = p.d.Builtins[e.Builtin]
		}
		p.w.tok(name)
		p.w.glue = true
		p.w.tok("(")
		for i, a := range e.Args {
			if i > 0 {
				p.w.tok(",")
			}
			p.expr(a)
		}
		p.w.tok(")")
	case *Index:
		_, isUn := e.X.(*Unary)
		lit, isLit := e.X.(*IntLit)
		p.operand(e.X, needsParensAsOperand(e.X) || isUn || (isLit && lit.V < 0))
		p.w.glue = true
		p.w.tok("[")
		p.expr(e.I)
		p.w.tok("]")
	case *Unary:
		if e.Op == UNeg {
			p.w.unaryMinus()
			_, isUn := e.X.(*Unary)
			lit, isLit := e.X.(*IntLit)
			p.operand(e.X, needsParensAsOperand(e.X) || isUn || (isLit && lit.V < 0))
		} else {
			p.w.tok(p.d.Word(RNot))
			p.operand(e.X, needsParensAsOperand(e.X))
		}
	case *Binary:
		pp := p.d.BinPrec(e.Op)
		p.operand(e.L, p.childNeedsParens(e.L, pp, true))
		p.w.tok(p.d.BinOpText(e.Op))
		p.operand(e.R, p.childNeedsParens(e.R, pp, false))
	default:
		panic("print: unknown expression")
	}
}

func needsParensAsOperand(e Expr) bool {
	_, ok := e.(*Binary)
	return ok
}

func (p *printer) childNeedsParens(child Expr, parentPrec int, left bool) bool {
	b, ok := child.(*Binary)
	if !ok {
		return false
	}
	cp := p.d.BinPrec(b.Op)
	if cp != parentPrec {
		return cp < parentPrec
	}
	if p.d.RightAssoc() {
		return left
	}
	return !left
}

func (p *printer) operand(e Expr, parens bool) {
	if parens {
		p.w.tok("(")
		p.expr(e)
		p.w.tok(")")
		return
	}
	p.expr(e)
}
