package lower

import (
	"strings"
	"testing"

	"utopia/internal/gen"
	"utopia/internal/lang"
	"utopia/internal/vm"
)

// Programs that print only integers and strings, so their output is the same
// in every dialect.
var programs = map[string]string{
	"division": `
func div(a, b) { return a / b; }
let pairs = [7, 2, -7, 2, 7, -2, -7, -2, 6, 3, -6, 3, 0, 5, 1, 7, -1, 7, 123, 10, -123, 10];
for (let i = 0; i < len(pairs); i = i + 2) {
  let a = pairs[i];
  let b = pairs[i + 1];
  print a & " " & b & ": " & (a / b) & " " & (a % b) & " " & div(a, b) & " " & ((a + 100) % b);
}
`,
	"loops": `
let total = 0;
count i from 1 to 10 { total = total + i; }
print total;
count i from 10 to 1 step -3 { write i & " "; }
print "";
for (let j = 0; j < 5; j = j + 1) {
  if (j == 1) { continue; }
  if (j == 4) { break; }
  write j;
}
print "";
let k = 0;
while (true) { k = k + 1; if (k > 6) { break; } if (k % 2 == 0) { continue; } write k; }
print "";
repeat { k = k - 1; } until (k <= 2);
do { k = k - 1; write k; } while (k > 0);
print "";
count a from 1 to 3 { count b from 1 to a { if (b == 2) { continue; } write a & b & ","; } }
print "";
`,
	"branches": `
func classify(n) {
  if (n < 0) { return "neg"; } else if (n == 0) { return "zero"; } else if (n < 10) { return "small"; } else { return "big"; }
}
func name(d) {
  let s = "?";
  switch (d) {
  case 1, 7: s = "weekend";
  case 2: s = "mon";
  case 3: s = "tue";
  default: s = "other";
  }
  return s;
}
print classify(-5) & classify(0) & classify(3) & classify(42);
count d from 1 to 8 { write name(d) & " "; }
print "";
switch ("b") { case "a": print "A"; case "b": print "B"; }
switch (99) { case 1: print "one"; }
print 1 & 2;
`,
	"lists": `
func sum(xs) {
  let t = 0;
  for (let i = 0; i < len(xs); i = i + 1) { t = t + xs[i]; }
  return t;
}
let xs = [5, 3, 8];
push(xs, 4);
xs[0] = 1;
print sum(xs);
print xs[len(xs) - 1];
let s = "hello";
print s[1] & s[4] & len(s);
let line = readline();
let total = 0;
while (line != none) { total = total + num(line); line = readline(); }
print "input " & total;
func fib(n) { if (n < 2) { return n; } return fib(n - 1) + fib(n - 2); }
print fib(15);
print 8 / 2 & " " & 9 % 3;
`,
}

const input = "1\n2\n39\n"

func run(t *testing.T, d *lang.Dialect, src string) string {
	t.Helper()
	var out strings.Builder
	if err := vm.RunSource(d, src, vm.Options{Stdin: strings.NewReader(input), Stdout: &out}); err != nil {
		t.Fatalf("run failed: %v\n--- source ---\n%s", err, src)
	}
	return out.String()
}

func TestLowerPreservesOutput(t *testing.T) {
	canon := gen.Canonical()
	for name, src := range programs {
		prog, err := lang.Parse(canon, src)
		if err != nil {
			t.Fatalf("%s: %v", name, err)
		}
		want := run(t, canon, src)
		for seed := uint64(1); seed <= 400; seed++ {
			d := gen.Generate(gen.Options{Seed: seed})
			low, err := Lower(d, prog, Options{})
			if err != nil {
				t.Fatalf("%s seed %d: %v", name, seed, err)
			}
			text := lang.Format(d, low)
			reparsed, err := lang.Parse(d, text)
			if err != nil {
				t.Fatalf("%s seed %d: reparse: %v\n%s", name, seed, err, text)
			}
			if again := lang.Format(d, reparsed); again != text {
				t.Fatalf("%s seed %d: print/parse round trip differs\n--- first ---\n%s\n--- second ---\n%s", name, seed, text, again)
			}
			if got := run(t, d, text); got != want {
				t.Fatalf("%s seed %d (%+v %+v): output differs\n--- want ---\n%s--- got ---\n%s--- source ---\n%s", name, seed, d.Styles, d.Sem, want, got, text)
			}
		}
	}
}
