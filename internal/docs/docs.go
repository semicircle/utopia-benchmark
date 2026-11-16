// Package docs renders a dialect's language reference from one fixed English
// template (reference.md.tmpl). Syntax blocks are drawn from the same shapes
// the parser uses, and every example's output is produced by running it, so
// the docs cannot drift from the toolchain.
package docs

import (
	"bytes"
	_ "embed"
	"fmt"
	"sort"
	"strings"
	"text/template"

	"utopia/internal/gen"
	. "utopia/internal/lang"
	"utopia/internal/lower"
	"utopia/internal/vm"
)

//go:embed reference.md.tmpl
var referenceTmpl string

type Example struct {
	Code   string
	Input  string
	Output string
}

type Row struct{ A, B string }

type Data struct {
	D       *Dialect
	Name    string
	Bin     string
	Ext     string
	Term    string
	Comment string
	Assign  string
	Eq, Ne  string
	Concat  string
	ModOp   string
	True    string
	False   string
	None    string
	And     string
	Or      string
	Not     string
	Let     string
	Print   string
	Write   string
	Return  string
	Break   string
	Cont    string

	Keywords []Row
	Builtins []Row
	Sem      Semantics
	Styles   Styles
	Has      map[string]bool
	Syntax   map[string]string
	Notes    map[string][]string
	Ex       map[string]Example
	Prec     string

	DispatchElse string
}

type syntaxRef struct {
	Syntax map[string]string
	Notes  map[string][]string
	Key    string
}

// BinName is the file name of the dialect's toolchain binary.
func BinName(d *Dialect) string { return strings.ToLower(d.Name) }

// Render produces the complete reference for d.
func Render(d *Dialect) (string, error) {
	data := &Data{
		D: d, Name: d.Name, Bin: BinName(d), Ext: d.Ext, Term: d.Terminator, Comment: d.Comment,
		Assign: d.Ops.Assign, Eq: d.Ops.Eq, Ne: d.Ops.Ne, Concat: d.Ops.Concat, ModOp: d.BinOpText(BMod),
		True: d.Word(RTrue), False: d.Word(RFalse), None: d.Word(RNone),
		And: d.Word(RAnd), Or: d.Word(ROr), Not: d.Word(RNot),
		Let: d.Word(RLet), Print: d.Word(RPrint), Write: d.Word(RWrite), Return: d.Word(RReturn),
		Break: d.Word(RBreak), Cont: d.Word(RContinue),
		Sem: d.Sem, Styles: d.Styles, Prec: string(d.Sem.Prec),
		DispatchElse: d.Word(RElse),
		Has:          map[string]bool{}, Syntax: map[string]string{}, Notes: map[string][]string{}, Ex: map[string]Example{},
	}
	for _, c := range ConstructOrder {
		if d.Has(c) {
			data.Has[string(c)] = true
			data.Syntax[string(c)], data.Notes[string(c)] = Syntax(d, c)
		}
	}
	data.Keywords = keywordRows(d)
	for _, b := range AllBuiltins {
		data.Builtins = append(data.Builtins, Row{d.Builtins[b], builtinDoc(d, b)})
	}
	if err := buildExamples(d, data); err != nil {
		return "", err
	}
	t, err := template.New("ref").Funcs(template.FuncMap{
		"dict": func(d *Data, key string) syntaxRef { return syntaxRef{d.Syntax, d.Notes, key} },
	}).Parse(referenceTmpl)
	if err != nil {
		return "", err
	}
	var buf bytes.Buffer
	if err := t.Execute(&buf, data); err != nil {
		return "", err
	}
	return tidy(buf.String()), nil
}

// tidy collapses runs of blank lines left by template conditionals.
func tidy(s string) string {
	for strings.Contains(s, "\n\n\n") {
		s = strings.ReplaceAll(s, "\n\n\n", "\n\n")
	}
	return strings.TrimSpace(s) + "\n"
}

var constructNames = map[Construct]string{
	CLet: "variable declaration", CAssign: "assignment", CIndexAssign: "element assignment",
	CCallStmt: "call statement", CPrint: "print statement", CWrite: "write statement",
	CReturn: "return statement", CBreak: "break statement", CContinue: "continue statement",
	CLabel: "label", CGoto: "jump", CJumpIf: "conditional jump", CIf: "if statement",
	CSwitch: "switch statement", CDispatch: "dispatch statement", CWhile: "while loop",
	CDoWhile: "do-while loop", CRepeatUntil: "repeat-until loop", CCFor: "for loop",
	CCountFor: "counting loop", CFunc: "function declaration",
}

var roleMeaning = map[Role]string{
	RTrue: "the boolean value true", RFalse: "the boolean value false", RNone: "the value none",
	RAnd: "logical and", ROr: "logical or", RNot: "logical not", RMod: "remainder operator",
}

func keywordRows(d *Dialect) []Row {
	uses := map[Role][]string{}
	for _, c := range ConstructOrder {
		shape, ok := d.Shapes[c]
		if !ok {
			continue
		}
		set := map[Role]bool{}
		ShapeRoles(shape, set)
		for r := range set {
			uses[r] = append(uses[r], constructNames[c])
		}
	}
	var rows []Row
	for _, r := range d.UsedRoles() {
		meaning := roleMeaning[r]
		if u := uses[r]; len(u) > 0 {
			meaning = "part of: " + strings.Join(u, ", ")
		}
		rows = append(rows, Row{d.Word(r), meaning})
	}
	sort.Slice(rows, func(i, j int) bool { return rows[i].A < rows[j].A })
	return rows
}

func builtinDoc(d *Dialect, b Builtin) string {
	none := d.Word(RNone)
	switch b {
	case BLen:
		return "`(x)`: the number of elements of list `x`, or the number of characters of string `x`."
	case BPush:
		return fmt.Sprintf("`(xs, v)`: appends `v` to the end of list `xs` (changing it) and returns %s.", "`"+none+"`")
	case BStr:
		return "`(v)`: converts any value to the string that printing it would show."
	case BNum:
		return "`(s)`: converts a string of decimal digits (optionally with a leading `-`, surrounding spaces allowed) to an integer. An integer is returned unchanged. Anything else is an error."
	case BReadline:
		return fmt.Sprintf("`()`: reads the next line of standard input and returns it as a string without the line ending, or `%s` when there is no more input.", none)
	}
	return ""
}

// ---- syntax blocks ----

var placeholders = map[string]string{
	"cond": "condition", "value": "expression", "subject": "expression", "from": "start",
	"to": "limit", "step": "step", "var": "name", "name": "name", "label": "label",
	"index": "index", "a": "argument", "v": "literal", "p": "parameter", "init": "initializer",
	"post": "update", "body": "statements", "then": "statements", "fn": "function",
}

func ph(slot string) string { return "<" + placeholders[slot] + ">" }

// Syntax renders a construct's shape as a pattern, plus notes on its
// optional and repeated parts.
func Syntax(d *Dialect, c Construct) (string, []string) {
	var notes []string
	var sb strings.Builder
	ind := 0
	line := []string{}
	glue := false
	flush := func() {
		if len(line) > 0 {
			sb.WriteString(strings.Repeat("    ", ind) + strings.Join(line, "") + "\n")
		}
		line = nil
	}
	tok := func(t string) {
		if len(line) > 0 && !glue && !noSpace(t, d.Terminator) && !strings.HasSuffix(line[len(line)-1], "(") && !strings.HasSuffix(line[len(line)-1], "[") {
			line = append(line, " ")
		}
		line = append(line, t)
		glue = false
	}
	var render func(parts []Part, top bool)
	render = func(parts []Part, top bool) {
		prev := PartKind(255)
		for _, p := range parts {
			switch p.Kind {
			case PKw:
				tok(d.Word(p.Role))
			case PPunct:
				if (p.Text == "(" || p.Text == "[") && (prev == PIdent || prev == PSame) {
					glue = true
				}
				tok(p.Text)
			case PTerm:
				tok(d.Terminator)
			case PExpr, PLit, PIdent, PSame, PSimple:
				tok(ph(p.Slot))
			case PBody:
				flush()
				ind++
				tok(ph(p.Slot))
				flush()
				ind--
			case POpt, PRep:
				if p.NL {
					flush()
				}
				lead := leadText(d, p.Sub)
				if len(p.Sub) == 1 && p.Sub[0].Kind == PExpr {
					notes = append(notes, fmt.Sprintf("`%s` is optional.", ph(p.Sub[0].Slot)))
				} else if p.Kind == PRep {
					notes = append(notes, fmt.Sprintf("The %s part may appear any number of times, including not at all.", lead))
				} else {
					notes = append(notes, fmt.Sprintf("The %s part is optional.", lead))
				}
				render(p.Sub, false)
			case PList:
				render(p.Sub, false)
				tok(p.Text)
				tok("...")
				if p.Min == 0 {
					notes = append(notes, fmt.Sprintf("The list of %ss may be empty.", strings.Trim(ph(firstSlot(p.Sub)), "<>")))
				}
			}
			prev = p.Kind
		}
	}
	render(d.Shapes[c], true)
	flush()
	if c == CCountFor {
		for _, p := range d.Shapes[c] {
			if p.Kind == PSame {
				notes = append(notes, fmt.Sprintf("The name after `%s` must be the loop variable.", d.Word(RNext)))
			}
		}
	}
	if c == CCFor {
		notes = append(notes, fmt.Sprintf("`<initializer>` and `<update>` are each a declaration or assignment written without the final `%s`; either may be left out.", d.Terminator))
	}
	return strings.TrimRight(sb.String(), "\n"), notes
}

func firstSlot(parts []Part) string {
	for _, p := range parts {
		if p.Slot != "" {
			return p.Slot
		}
	}
	return ""
}

func noSpace(t, term string) bool {
	switch t {
	case ")", "]", ",", ":", ";":
		return true
	}
	return t == term
}

// leadText names a group by its leading tokens, e.g. "`else if`".
func leadText(d *Dialect, parts []Part) string {
	var words []string
	for _, p := range parts {
		switch p.Kind {
		case PKw:
			words = append(words, d.Word(p.Role))
			continue
		case PPunct:
			if len(words) == 0 {
				words = append(words, p.Text)
				continue
			}
		case PExpr, PLit, PIdent:
			if len(words) == 0 {
				words = append(words, ph(p.Slot))
			}
		case PList:
			if len(words) == 0 {
				words = append(words, ph(firstSlot(p.Sub)))
			}
		}
		break
	}
	return "`" + strings.Join(words, " ") + " ...`"
}

// ---- examples ----

// example lowers a canonical program into d, then runs it for its output.
func example(d *Dialect, src, input string, raw bool) (Example, error) {
	canon := gen.Canonical()
	prog, err := Parse(canon, src)
	if err != nil {
		return Example{}, fmt.Errorf("docs example does not parse: %v\n%s", err, src)
	}
	low, err := lower.Lower(d, prog, lower.Options{Raw: raw})
	if err != nil {
		return Example{}, err
	}
	return runExample(d, Format(d, low), input)
}

func runExample(d *Dialect, code, input string) (Example, error) {
	var out bytes.Buffer
	err := vm.RunSource(d, code, vm.Options{Stdin: strings.NewReader(input), Stdout: &out})
	o := out.String()
	if err != nil {
		if _, isRuntime := err.(*vm.RuntimeError); !isRuntime {
			return Example{}, fmt.Errorf("docs example fails to compile in %s: %v\n%s", d.Name, err, code)
		}
		o += "error: " + err.Error() + "\n"
	}
	return Example{Code: strings.TrimRight(code, "\n"), Input: input, Output: strings.TrimRight(o, "\n")}, nil
}

// line builds one dialect statement from source pieces, for knob demos that
// must be shown exactly as the dialect parses them.
func stmtLine(d *Dialect, role Role, expr string) string {
	return d.Word(role) + " " + expr + d.Terminator
}

func buildExamples(d *Dialect, data *Data) error {
	type spec struct {
		key, src, input string
		raw             bool
	}
	specs := []spec{
		{key: "hello", src: `print "Hello, world!";`},
		{key: "vars", src: `
let x = 5;
x = x + 2;
let name = "Ada";
print name & " has " & x & " apples";
let flag = x > 6;
print flag;
print none;`},
		{key: "argorder", src: `
func show(x) { print "evaluating " & x; return x; }
func pair(a, b) { return a & b; }
print pair(show(1), show(2));`},
		{key: "operandorder", src: `
func show(x) { print "evaluating " & x; return x; }
print show(10) - show(4);`},
		{key: "shortcircuit", src: `
func check(name, result) { print "checking " & name; return result; }
if (check("left", true) or check("right", false)) { print "yes"; }
if (check("left", false) and check("right", true)) { print "yes"; } else { print "no"; }`},
		{key: "index", raw: true, src: `
let xs = [10, 20, 30];
print xs[1];
xs[1] = 99;
print xs;
let word = "abc";
print word[1];`},
		{key: "listeq", src: `
let a = [1, 2];
let b = [1, 2];
let c = a;
push(c, 3);
print a;
if (a == c) { print "a equals c"; }
if (a == [1, 2, 3]) { print "a equals a new list with the same elements"; } else { print "a does not equal a new list with the same elements"; }`},
		{key: "if", src: `
let n = 7;
if (n < 5) { print "small"; } else if (n < 10) { print "medium"; } else { print "large"; }`},
		{key: "switch", src: `
count d from 1 to 4 {
  switch (d) {
  case 1: print "one";
  case 2, 3: print "two or three";
  default: print "something else";
  }
}`},
		{key: "while", src: `
let n = 1;
while (n < 100) { n = n * 2; }
print n;`},
		{key: "posttest", src: `
let n = 0;
repeat { n = n + 3; } until (n > 10);
print n;`},
		{key: "cfor", src: `
for (let i = 0; i < 3; i = i + 1) { print i; }`},
		{key: "count", src: `
count i from 1 to 5 { write i & " "; }
print "";
count i from 10 to 1 step -3 { write i & " "; }
print "";`},
		{key: "breakcont", src: `
count i from 1 to 10 {
  if (i % 2 == 0) { continue; }
  if (i > 7) { break; }
  write i & " ";
}
print "";`},
		{key: "labels", src: `
let i = 1;
while (i <= 5) { write i & " "; i = i + 1; }
print "";`},
		{key: "func", src: `
func square(x) { return x * x; }
func fact(n) {
  if (n <= 1) { return 1; }
  return n * fact(n - 1);
}
func greet(name) { print "Hello, " & name; }
print square(7);
print fact(10);
greet("Lin");
let r = greet("Max");
print r;`},
		{key: "listshare", src: `
func addOne(xs) { push(xs, 1); }
let mine = [5];
addOne(mine);
print mine;`},
		{key: "builtins", input: "first line\nsecond line\n", src: `
let xs = [3, 1];
push(xs, 4);
print len(xs);
print len("hello");
print str(42) & "!";
print num("12") + 1;
print readline();
print readline();
print readline();`},
		{key: "complete", input: "4\n-2\n17\n9\n", src: `
let total = 0;
let seen = 0;
let best = 0;
let line = readline();
while (line != none) {
  let n = num(line);
  if (seen == 0) { best = n; } else if (n > best) { best = n; }
  total = total + n;
  seen = seen + 1;
  line = readline();
}
print "count " & seen;
print "sum " & total;
print "max " & best;`},
	}
	if d.Has(CSwitch) && d.Styles.Switch == StyleC && d.Sem.SwitchFallthrough {
		specs = append(specs, spec{key: "fallthrough", raw: true, src: `
switch (2) {
case 1: print "one";
case 2: print "two";
case 3: print "three";
default: print "other";
}`})
	}
	if d.Sem.OutOfRange == OORWrap {
		specs = append(specs, spec{key: "wrap", raw: true, src: `
let xs = [10, 20, 30];
print xs[3];
print xs[4];
print xs[-1];`})
	}
	for _, s := range specs {
		ex, err := example(d, s.src, s.input, s.raw)
		if err != nil {
			return fmt.Errorf("%s: %w", s.key, err)
		}
		data.Ex[s.key] = ex
	}

	// Demos written directly in the dialect, so they show exactly how its
	// own parser groups and evaluates them.
	demo := func(key string, lines ...string) error {
		ex, err := runExample(d, strings.Join(lines, "\n")+"\n", "")
		if err != nil {
			return fmt.Errorf("%s: %w", key, err)
		}
		data.Ex[key] = ex
		return nil
	}
	mod := d.BinOpText(BMod)
	if err := demo("prec",
		stmtLine(d, RPrint, "2 + 3 * 4"),
		stmtLine(d, RPrint, "10 - 4 - 3"),
		stmtLine(d, RPrint, "(2 + 3) * 4"),
		stmtLine(d, RPrint, "2 + (3 * 4)"),
	); err != nil {
		return err
	}
	if err := demo("div",
		stmtLine(d, RPrint, "7 / 2"),
		stmtLine(d, RPrint, "-7 / 2"),
		stmtLine(d, RPrint, "7 "+mod+" 2"),
		stmtLine(d, RPrint, "-7 "+mod+" 2"),
		stmtLine(d, RPrint, "6 / 3"),
	); err != nil {
		return err
	}
	if err := demo("concat",
		stmtLine(d, RPrint, `"n = " `+d.Ops.Concat+` 5`),
		stmtLine(d, RPrint, `"a" `+d.Ops.Concat+` "b" `+d.Ops.Concat+` "c"`),
	); err != nil {
		return err
	}
	if err := demo("errors", stmtLine(d, RPrint, `"before"`), stmtLine(d, RPrint, "1 / 0"), stmtLine(d, RPrint, `"after"`)); err != nil {
		return err
	}
	return nil
}
