package vm

import (
	"bufio"
	"fmt"
	"io"
	"strconv"
	"strings"

	. "utopia/internal/lang"
)

// RuntimeError is an error raised while a program runs.
type RuntimeError struct {
	Line int
	Msg  string
}

func (e *RuntimeError) Error() string { return fmt.Sprintf("line %d: %s", e.Line, e.Msg) }

type Options struct {
	Stdin    io.Reader
	Stdout   io.Writer
	MaxSteps int64 // 0 means the default
	MaxDepth int   // 0 means the default
}

const (
	DefaultMaxSteps = 50_000_000
	DefaultMaxDepth = 10_000
)

type frame struct {
	fn   *Func
	ip   int
	base int
}

type machine struct {
	d     *Dialect
	mod   *Module
	stack []Value
	in    *bufio.Reader
	out   *bufio.Writer
	line  int
}

// Run executes a compiled module. Output is flushed even when it fails.
func Run(d *Dialect, mod *Module, opt Options) error {
	if opt.MaxSteps == 0 {
		opt.MaxSteps = DefaultMaxSteps
	}
	if opt.MaxDepth == 0 {
		opt.MaxDepth = DefaultMaxDepth
	}
	if opt.Stdin == nil {
		opt.Stdin = strings.NewReader("")
	}
	m := &machine{d: d, mod: mod, in: bufio.NewReader(opt.Stdin), out: bufio.NewWriter(opt.Stdout)}
	defer m.out.Flush()
	return m.run(opt)
}

func (m *machine) fail(format string, args ...any) error {
	return &RuntimeError{Line: m.line, Msg: fmt.Sprintf(format, args...)}
}

func (m *machine) push(v Value) { m.stack = append(m.stack, v) }
func (m *machine) pop() Value {
	v := m.stack[len(m.stack)-1]
	m.stack = m.stack[:len(m.stack)-1]
	return v
}

func (m *machine) wantBool(v Value, what string) (bool, error) {
	if v.K != KBool {
		return false, m.fail("%s must be %s or %s, got %s %s", what, m.d.Word(RTrue), m.d.Word(RFalse), typeName(v), display(m.d, v, true))
	}
	return v.I != 0, nil
}

func (m *machine) wantInts(a, b Value, op string) error {
	if a.K != KInt || b.K != KInt {
		return m.fail("`%s` needs two integers, got %s and %s", op, typeName(a), typeName(b))
	}
	return nil
}

func reverse(vs []Value) {
	for i, j := 0, len(vs)-1; i < j; i, j = i+1, j-1 {
		vs[i], vs[j] = vs[j], vs[i]
	}
}

func (m *machine) run(opt Options) error {
	main := m.mod.Funcs[m.mod.Main]
	m.stack = make([]Value, main.NLocals, 1024)
	frames := []frame{{fn: main, base: 0}}
	var steps int64
	for {
		f := &frames[len(frames)-1]
		in := f.fn.Code[f.ip]
		f.ip++
		m.line = int(in.Line)
		steps++
		if steps > opt.MaxSteps {
			return m.fail("step limit exceeded (%d steps); is there an infinite loop?", opt.MaxSteps)
		}
		switch in.Op {
		case OpConst:
			m.push(m.mod.Consts[in.A])
		case OpNone:
			m.push(NoneVal())
		case OpLoad:
			v := m.stack[f.base+int(in.A)]
			if v.K == KUnset {
				return m.fail("variable `%s` is used before it has a value", f.fn.Locals[in.A])
			}
			m.push(v)
		case OpStore:
			m.stack[f.base+int(in.A)] = m.pop()
		case OpPop:
			m.pop()
		case OpSwap:
			n := len(m.stack)
			m.stack[n-1], m.stack[n-2] = m.stack[n-2], m.stack[n-1]
		case OpAdd, OpSub, OpMul, OpDiv, OpMod, OpConcat, OpLt, OpLe, OpGt, OpGe, OpEq, OpNe, OpAnd, OpOr:
			b := m.pop()
			a := m.pop()
			v, err := m.binary(in.Op, a, b)
			if err != nil {
				return err
			}
			m.push(v)
		case OpNot:
			b, err := m.wantBool(m.pop(), "the operand of `"+m.d.Word(RNot)+"`")
			if err != nil {
				return err
			}
			m.push(BoolVal(!b))
		case OpNeg:
			v := m.pop()
			if v.K != KInt {
				return m.fail("cannot negate a %s", typeName(v))
			}
			m.push(IntVal(-v.I))
		case OpCheckBool:
			if _, err := m.wantBool(m.stack[len(m.stack)-1], "the operand of a logical operator"); err != nil {
				return err
			}
		case OpJump:
			f.ip = int(in.A)
		case OpJumpIfFalse, OpJumpIfTrue:
			b, err := m.wantBool(m.pop(), "a condition")
			if err != nil {
				return err
			}
			if b == (in.Op == OpJumpIfTrue) {
				f.ip = int(in.A)
			}
		case OpJumpIfFalseKeep, OpJumpIfTrueKeep:
			b, err := m.wantBool(m.stack[len(m.stack)-1], "the operand of a logical operator")
			if err != nil {
				return err
			}
			if b == (in.Op == OpJumpIfTrueKeep) {
				f.ip = int(in.A)
			}
		case OpCall:
			if len(frames) >= opt.MaxDepth {
				return m.fail("too many nested calls (limit %d); is there runaway recursion?", opt.MaxDepth)
			}
			callee := m.mod.Funcs[in.A]
			base := len(m.stack) - int(in.B)
			if in.C == 1 {
				reverse(m.stack[base:])
			}
			for i := callee.NParams; i < callee.NLocals; i++ {
				m.push(Value{})
			}
			frames = append(frames, frame{fn: callee, base: base})
		case OpRet:
			ret := m.pop()
			m.stack = m.stack[:f.base]
			frames = frames[:len(frames)-1]
			m.push(ret)
		case OpHalt:
			return nil
		case OpBuiltin:
			n := int(in.B)
			args := append([]Value(nil), m.stack[len(m.stack)-n:]...)
			m.stack = m.stack[:len(m.stack)-n]
			if in.C == 1 {
				reverse(args)
			}
			v, err := m.builtin(Builtin(in.A), args)
			if err != nil {
				return err
			}
			m.push(v)
		case OpPrint:
			m.out.WriteString(display(m.d, m.pop(), false))
			if in.A == 1 {
				m.out.WriteByte('\n')
			}
		case OpList:
			n := int(in.A)
			elems := append([]Value(nil), m.stack[len(m.stack)-n:]...)
			m.stack = m.stack[:len(m.stack)-n]
			m.push(Value{K: KList, L: &ListObj{Elems: elems}})
		case OpIndex:
			i := m.pop()
			x := m.pop()
			v, err := m.index(x, i)
			if err != nil {
				return err
			}
			m.push(v)
		case OpSetIndex:
			v := m.pop()
			i := m.pop()
			x := m.pop()
			if x.K == KStr {
				return m.fail("strings cannot be changed in place")
			}
			if x.K != KList {
				return m.fail("cannot index a %s", typeName(x))
			}
			k, err := m.position(i, len(x.L.Elems))
			if err != nil {
				return err
			}
			x.L.Elems[k] = v
		case OpCheckStep:
			v := m.stack[len(m.stack)-1]
			if v.K != KInt {
				return m.fail("loop step must be an integer, got %s", typeName(v))
			}
			if v.I == 0 {
				return m.fail("loop step cannot be 0")
			}
		case OpForCond:
			step := m.pop()
			limit := m.pop()
			v := m.pop()
			if v.K != KInt || limit.K != KInt {
				return m.fail("loop bounds must be integers, got %s and %s", typeName(v), typeName(limit))
			}
			var ok bool
			switch {
			case step.I > 0 && in.A == 1:
				ok = v.I <= limit.I
			case step.I > 0:
				ok = v.I < limit.I
			case in.A == 1:
				ok = v.I >= limit.I
			default:
				ok = v.I > limit.I
			}
			m.push(BoolVal(ok))
		default:
			return m.fail("internal error: bad opcode %d", in.Op)
		}
	}
}

func (m *machine) toText(v Value) string { return display(m.d, v, false) }

func (m *machine) binary(op Op, a, b Value) (Value, error) {
	switch op {
	case OpAdd:
		if m.d.Ops.Concat == "+" && (a.K == KStr || b.K == KStr) {
			return StrVal(m.toText(a) + m.toText(b)), nil
		}
		if err := m.wantInts(a, b, "+"); err != nil {
			return Value{}, err
		}
		return IntVal(a.I + b.I), nil
	case OpConcat:
		return StrVal(m.toText(a) + m.toText(b)), nil
	case OpSub:
		if err := m.wantInts(a, b, "-"); err != nil {
			return Value{}, err
		}
		return IntVal(a.I - b.I), nil
	case OpMul:
		if err := m.wantInts(a, b, "*"); err != nil {
			return Value{}, err
		}
		return IntVal(a.I * b.I), nil
	case OpDiv, OpMod:
		name := "/"
		if op == OpMod {
			name = m.d.BinOpText(BMod)
		}
		if err := m.wantInts(a, b, name); err != nil {
			return Value{}, err
		}
		if b.I == 0 {
			return Value{}, m.fail("division by zero")
		}
		q := divide(m.d.Sem.Div, a.I, b.I)
		if op == OpDiv {
			return IntVal(q), nil
		}
		return IntVal(a.I - b.I*q), nil
	case OpEq:
		return BoolVal(equal(m.d.Sem.ListEqStructural, a, b)), nil
	case OpNe:
		return BoolVal(!equal(m.d.Sem.ListEqStructural, a, b)), nil
	case OpLt, OpLe, OpGt, OpGe:
		var c int
		switch {
		case a.K == KInt && b.K == KInt:
			c = cmpInt(a.I, b.I)
		case a.K == KStr && b.K == KStr:
			c = strings.Compare(a.S, b.S)
		default:
			return Value{}, m.fail("cannot compare %s with %s", typeName(a), typeName(b))
		}
		switch op {
		case OpLt:
			return BoolVal(c < 0), nil
		case OpLe:
			return BoolVal(c <= 0), nil
		case OpGt:
			return BoolVal(c > 0), nil
		}
		return BoolVal(c >= 0), nil
	case OpAnd, OpOr:
		x, err := m.wantBool(a, "the operand of a logical operator")
		if err != nil {
			return Value{}, err
		}
		y, err := m.wantBool(b, "the operand of a logical operator")
		if err != nil {
			return Value{}, err
		}
		if op == OpAnd {
			return BoolVal(x && y), nil
		}
		return BoolVal(x || y), nil
	}
	return Value{}, m.fail("internal error: bad operator")
}

func cmpInt(a, b int64) int {
	switch {
	case a < b:
		return -1
	case a > b:
		return 1
	}
	return 0
}

// divide implements the dialect's integer division rounding.
func divide(mode DivMode, a, b int64) int64 {
	q := a / b
	inexact := a%b != 0
	sameSign := (a < 0) == (b < 0)
	switch mode {
	case DivFloor:
		if inexact && !sameSign {
			q--
		}
	case DivCeil:
		if inexact && sameSign {
			q++
		}
	}
	return q
}

// position maps a user-visible index to a 0-based slice position.
func (m *machine) position(i Value, n int) (int, error) {
	if i.K != KInt {
		return 0, m.fail("index must be an integer, got %s", typeName(i))
	}
	base := int64(m.d.Sem.IndexBase)
	k := i.I - base
	if k >= 0 && k < int64(n) {
		return int(k), nil
	}
	if m.d.Sem.OutOfRange == OORWrap && n > 0 {
		k %= int64(n)
		if k < 0 {
			k += int64(n)
		}
		return int(k), nil
	}
	if n == 0 {
		return 0, m.fail("index %d is out of range: the value is empty", i.I)
	}
	return 0, m.fail("index %d is out of range (valid: %d to %d)", i.I, base, base+int64(n)-1)
}

func (m *machine) index(x, i Value) (Value, error) {
	switch x.K {
	case KList:
		k, err := m.position(i, len(x.L.Elems))
		if err != nil {
			return Value{}, err
		}
		return x.L.Elems[k], nil
	case KStr:
		k, err := m.position(i, len(x.S))
		if err != nil {
			return Value{}, err
		}
		return StrVal(x.S[k : k+1]), nil
	}
	return Value{}, m.fail("cannot index a %s", typeName(x))
}

func (m *machine) builtin(b Builtin, args []Value) (Value, error) {
	name := m.d.Builtins[b]
	switch b {
	case BLen:
		switch args[0].K {
		case KList:
			return IntVal(int64(len(args[0].L.Elems))), nil
		case KStr:
			return IntVal(int64(len(args[0].S))), nil
		}
		return Value{}, m.fail("`%s` needs a list or string, got %s", name, typeName(args[0]))
	case BPush:
		if args[0].K != KList {
			return Value{}, m.fail("`%s` needs a list as its first argument, got %s", name, typeName(args[0]))
		}
		args[0].L.Elems = append(args[0].L.Elems, args[1])
		return NoneVal(), nil
	case BStr:
		return StrVal(m.toText(args[0])), nil
	case BNum:
		switch args[0].K {
		case KInt:
			return args[0], nil
		case KStr:
			n, err := strconv.ParseInt(strings.TrimSpace(args[0].S), 10, 64)
			if err != nil {
				return Value{}, m.fail("`%s` cannot convert %s to an integer", name, QuoteString(args[0].S))
			}
			return IntVal(n), nil
		}
		return Value{}, m.fail("`%s` needs a string, got %s", name, typeName(args[0]))
	case BReadline:
		line, err := m.in.ReadString('\n')
		if err != nil && line == "" {
			return NoneVal(), nil
		}
		return StrVal(strings.TrimRight(line, "\r\n")), nil
	}
	return Value{}, m.fail("internal error: bad builtin")
}

// RunSource parses, compiles and runs source text in one step.
func RunSource(d *Dialect, src string, opt Options) error {
	prog, err := Parse(d, src)
	if err != nil {
		return err
	}
	mod, err := Compile(d, prog)
	if err != nil {
		return err
	}
	return Run(d, mod, opt)
}
