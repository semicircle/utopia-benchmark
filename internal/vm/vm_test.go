package vm

import (
	"strings"
	"testing"

	"utopia/internal/gen"
	"utopia/internal/lang"
)

// canon returns the canonical dialect with one semantic change applied.
func canon(change func(*lang.Semantics)) *lang.Dialect {
	d := gen.Canonical()
	change(&d.Sem)
	return d
}

func run(t *testing.T, d *lang.Dialect, src string) string {
	t.Helper()
	var out strings.Builder
	err := RunSource(d, src, Options{Stdout: &out})
	if err != nil {
		out.WriteString("error: " + err.Error() + "\n")
	}
	return out.String()
}

func TestKnobs(t *testing.T) {
	cases := []struct {
		name   string
		change func(*lang.Semantics)
		src    string
		want   string
	}{
		{"div trunc", func(s *lang.Semantics) {}, `print -7 / 2; print -7 % 2; print 7 / -2;`, "-3\n-1\n-3\n"},
		{"div floor", func(s *lang.Semantics) { s.Div = lang.DivFloor }, `print -7 / 2; print -7 % 2; print 7 / -2; print 7 / 2;`, "-4\n1\n-4\n3\n"},
		{"div ceil", func(s *lang.Semantics) { s.Div = lang.DivCeil }, `print 7 / 2; print 7 % 2; print -7 / 2; print 6 / 3;`, "4\n-1\n-3\n2\n"},
		{"index base 1", func(s *lang.Semantics) { s.IndexBase = 1 }, `let xs = [10, 20]; print xs[1]; print xs[2]; print xs[0];`,
			"10\n20\nerror: line 1: index 0 is out of range (valid: 1 to 2)\n"},
		{"wrap", func(s *lang.Semantics) { s.OutOfRange = lang.OORWrap }, `let xs = [10, 20, 30]; print xs[3]; print xs[-1]; print "abc"[4];`, "10\n30\nb\n"},
		{"wrap base 1", func(s *lang.Semantics) { s.OutOfRange = lang.OORWrap; s.IndexBase = 1 }, `let xs = [10, 20, 30]; print xs[0]; print xs[4];`, "30\n10\n"},
		{"exclusive count", func(s *lang.Semantics) { s.CountInclusive = false }, `count i from 1 to 4 { write i; } print ""; count i from 4 to 1 step -1 { write i; } print "";`, "123\n432\n"},
		{"no short circuit", func(s *lang.Semantics) { s.ShortCircuit = false },
			`func f(x) { print x; return true; } if (f("a") or f("b")) { print "y"; }`, "a\nb\ny\n"},
		{"short circuit", func(s *lang.Semantics) {},
			`func f(x) { print x; return true; } if (f("a") or f("b")) { print "y"; }`, "a\ny\n"},
		{"args right to left", func(s *lang.Semantics) { s.ArgOrder = lang.RightToLeft },
			`func f(x) { print x; return x; } func g(a, b) { return a - b; } print g(f(10), f(3));`, "3\n10\n7\n"},
		{"operands right to left", func(s *lang.Semantics) { s.OperandOrder = lang.RightToLeft },
			`func f(x) { print x; return x; } print f(10) - f(3);`, "3\n10\n7\n"},
		{"list identity", func(s *lang.Semantics) { s.ListEqStructural = false }, `let a = [1]; let b = a; print a == b; print a == [1];`, "true\nfalse\n"},
		{"list structural", func(s *lang.Semantics) {}, `print [1, [2]] == [1, [2]]; print [1] == [2];`, "true\nfalse\n"},
		{"flat left", func(s *lang.Semantics) { s.Prec = lang.PrecFlatLeft }, `print 2 + 3 * 4; print 10 - 4 - 3;`, "20\n3\n"},
		{"flat right", func(s *lang.Semantics) { s.Prec = lang.PrecFlatRight }, `print 2 * 3 + 4; print 10 - 4 - 3;`, "14\n9\n"},
		{"strict conditions", func(s *lang.Semantics) {}, `if (1) { print "x"; }`, "error: line 1: a condition must be true or false, got integer 1\n"},
		{"step limit", func(s *lang.Semantics) {}, `while (true) { }`, "error: line 1: step limit exceeded (50000000 steps); is there an infinite loop?\n"},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			if got := run(t, canon(c.change), c.src); got != c.want {
				t.Errorf("got %q, want %q", got, c.want)
			}
		})
	}
}

func TestSwitchFallthrough(t *testing.T) {
	d := gen.Canonical()
	d.Styles.Switch = lang.StyleC
	d.Sem.SwitchFallthrough = true
	src := `switch (2) { case 1: print "one"; case 2: print "two"; case 3: print "three"; break; default: print "other"; }`
	if got := run(t, d, src); got != "two\nthree\n" {
		t.Errorf("got %q", got)
	}
}

func TestCompileErrors(t *testing.T) {
	d := gen.Canonical()
	for src, want := range map[string]string{
		`x = 1;`:                    "variable `x` is not declared",
		`print y;`:                  "unknown variable `y`",
		`func f(a) { } f(1, 2);`:    "`f` takes 1 argument(s), got 2",
		`func len(x) { return x; }`: "`len` is a builtin",
		`print 1`:                   "expected `;` but found end of file",
	} {
		_, err := lang.Parse(d, src)
		if err == nil {
			var prog *lang.Program
			prog, err = lang.Parse(d, src)
			if err == nil {
				_, err = Compile(d, prog)
			}
		}
		if want == "" {
			continue
		}
		if err == nil || !strings.Contains(err.Error(), want) {
			t.Errorf("%s: got %v, want %q", src, err, want)
		}
	}
}
