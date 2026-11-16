// Command utopia is the Utopia toolchain.
//
// Built normally, it is the researcher's tool: it generates dialects,
// workspaces and docs. Built with `utopia bake`, the seed is fixed at link
// time and the binary becomes that one language's toolchain, offering only
// `run` and `check`.
package main

import (
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"

	"utopia/internal/docs"
	"utopia/internal/gen"
	"utopia/internal/lang"
	"utopia/internal/lower"
	"utopia/internal/tasks"
	"utopia/internal/vm"
)

// Set with -ldflags by `utopia bake`.
var (
	bakedSeed string
	bakedSem  string
)

func main() {
	if bakedSeed != "" {
		os.Exit(bakedMain())
	}
	os.Exit(devMain())
}

func die(format string, args ...any) int {
	fmt.Fprintf(os.Stderr, "error: "+format+"\n", args...)
	return 1
}

// ---- baked: one language's toolchain ----

func bakedDialect() *lang.Dialect {
	seed, _ := strconv.ParseUint(bakedSeed, 10, 64)
	return gen.Generate(gen.Options{Seed: seed, Semantics: gen.SemanticsMode(bakedSem)})
}

func bakedMain() int {
	d := bakedDialect()
	bin := docs.BinName(d)
	usage := fmt.Sprintf("usage:\n  %s run FILE.%s     check and run a program\n  %s check FILE.%s   check a program without running it\n", bin, d.Ext, bin, d.Ext)
	if len(os.Args) != 3 || (os.Args[1] != "run" && os.Args[1] != "check") {
		fmt.Fprint(os.Stderr, usage)
		return 2
	}
	code := runFile(d, os.Args[2], os.Args[1] == "check")
	trace(os.Args[1], os.Args[2], code)
	return code
}

// trace appends one JSON line per invocation to the file named by
// UTOPIA_TRACE, when set. The harness uses it to count toolchain runs and
// failures, however the agent spelled the command.
func trace(cmd, path string, code int) {
	name := os.Getenv("UTOPIA_TRACE")
	if name == "" {
		return
	}
	f, err := os.OpenFile(name, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0o644)
	if err != nil {
		return
	}
	defer f.Close()
	line, _ := json.Marshal(map[string]any{"cmd": cmd, "file": path, "exit": code})
	f.Write(append(line, '\n'))
}

func runFile(d *lang.Dialect, path string, checkOnly bool) int {
	src, err := os.ReadFile(path)
	if err != nil {
		return die("%v", err)
	}
	prog, err := lang.Parse(d, string(src))
	if err != nil {
		return die("%v", err)
	}
	mod, err := vm.Compile(d, prog)
	if err != nil {
		return die("%v", err)
	}
	if checkOnly {
		fmt.Println("ok")
		return 0
	}
	if err := vm.Run(d, mod, vm.Options{Stdin: os.Stdin, Stdout: os.Stdout}); err != nil {
		return die("%v", err)
	}
	return 0
}

// ---- dev: the researcher's tool ----

const devUsage = `usage: utopia COMMAND [flags]

commands:
  gen     -seed N -out DIR [-bake]   create a workspace: docs, task prompts (and a baked toolchain)
  docs    -seed N                    print the language reference
  info    -seed N                    print the dialect's hidden settings as JSON
  render  -seed N FILE.canon         translate a canonical program into the dialect
  run     -seed N|-canon FILE        run a program
  check   -seed N|-canon FILE        check a program without running it
  bake    -seed N -o PATH            build a standalone toolchain for one dialect

common flags:
  -semantics random|standard   standard keeps conventional behavior (syntax-only novelty)
`

type common struct {
	fs        *flag.FlagSet
	seed      *uint64
	canon     *bool
	semantics *string
}

func newFlags(name string) common {
	fs := flag.NewFlagSet(name, flag.ExitOnError)
	return common{
		fs:        fs,
		seed:      fs.Uint64("seed", 0, "dialect seed (required unless -canon)"),
		canon:     fs.Bool("canon", false, "use the canonical dialect"),
		semantics: fs.String("semantics", "random", "random or standard"),
	}
}

func (c common) dialect() (*lang.Dialect, error) {
	if *c.canon {
		return gen.Canonical(), nil
	}
	if *c.seed == 0 {
		return nil, errors.New("-seed is required (a positive integer)")
	}
	mode := gen.SemanticsMode(*c.semantics)
	if mode != gen.SemRandom && mode != gen.SemStandard {
		return nil, fmt.Errorf("-semantics must be random or standard, not %q", *c.semantics)
	}
	return gen.Generate(gen.Options{Seed: *c.seed, Semantics: mode}), nil
}

func devMain() int {
	if len(os.Args) < 2 {
		fmt.Fprint(os.Stderr, devUsage)
		return 2
	}
	cmd, args := os.Args[1], os.Args[2:]
	f := newFlags(cmd)
	var out, tasksDir *string
	var bake *bool
	switch cmd {
	case "gen":
		out = f.fs.String("out", "", "workspace directory to create")
		tasksDir = f.fs.String("tasks", "tasks", "task directory")
		bake = f.fs.Bool("bake", false, "also build the dialect's toolchain into DIR/bin")
	case "bake":
		out = f.fs.String("o", "", "output binary path")
	case "docs", "info", "render", "run", "check":
	default:
		fmt.Fprint(os.Stderr, devUsage)
		return 2
	}
	f.fs.Parse(args)
	d, err := f.dialect()
	if err != nil {
		return die("%v", err)
	}
	switch cmd {
	case "docs":
		text, err := docs.Render(d)
		if err != nil {
			return die("%v", err)
		}
		fmt.Print(text)
	case "info":
		enc := json.NewEncoder(os.Stdout)
		enc.SetIndent("", "  ")
		enc.Encode(map[string]any{
			"name": d.Name, "ext": d.Ext, "seed": d.Seed, "styles": d.Styles,
			"semantics": d.Sem, "ops": d.Ops, "terminator": d.Terminator,
			"comment": d.Comment, "keywords": d.Keywords, "builtins": builtinNames(d),
		})
	case "render":
		if f.fs.NArg() != 1 {
			return die("render needs one canonical source file")
		}
		src, err := os.ReadFile(f.fs.Arg(0))
		if err != nil {
			return die("%v", err)
		}
		prog, err := lang.Parse(gen.Canonical(), string(src))
		if err != nil {
			return die("%v", err)
		}
		low, err := lower.Lower(d, prog, lower.Options{})
		if err != nil {
			return die("%v", err)
		}
		fmt.Print(lang.Format(d, low))
	case "run", "check":
		if f.fs.NArg() != 1 {
			return die("%s needs one source file", cmd)
		}
		return runFile(d, f.fs.Arg(0), cmd == "check")
	case "bake":
		if *out == "" {
			return die("bake needs -o PATH")
		}
		if err := bakeBinary(*f.seed, *f.semantics, *out); err != nil {
			return die("%v", err)
		}
	case "gen":
		if *out == "" {
			return die("gen needs -out DIR")
		}
		if err := genWorkspace(d, *f.seed, *f.semantics, *tasksDir, *out, *bake); err != nil {
			return die("%v", err)
		}
		fmt.Printf("created a %s workspace in %s\n", d.Name, *out)
	}
	return 0
}

func builtinNames(d *lang.Dialect) map[string]string {
	names := map[lang.Builtin]string{lang.BLen: "len", lang.BPush: "push", lang.BStr: "str", lang.BNum: "num", lang.BReadline: "readline"}
	out := map[string]string{}
	for b, w := range d.Builtins {
		out[names[b]] = w
	}
	return out
}

// moduleRoot finds the directory holding go.mod, starting from the current
// directory, so bake can compile this toolchain from source.
func moduleRoot() (string, error) {
	dir, err := os.Getwd()
	if err != nil {
		return "", err
	}
	for {
		if _, err := os.Stat(filepath.Join(dir, "go.mod")); err == nil {
			return dir, nil
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			return "", errors.New("bake must run inside the utopia source tree (go.mod not found)")
		}
		dir = parent
	}
}

func bakeBinary(seed uint64, semantics, out string) error {
	root, err := moduleRoot()
	if err != nil {
		return err
	}
	abs, err := filepath.Abs(out)
	if err != nil {
		return err
	}
	ldflags := fmt.Sprintf("-s -w -X main.bakedSeed=%d -X main.bakedSem=%s", seed, semantics)
	cmd := exec.Command("go", "build", "-trimpath", "-ldflags", ldflags, "-o", abs, "./cmd/utopia")
	cmd.Dir = root
	cmd.Stdout, cmd.Stderr = os.Stdout, os.Stderr
	return cmd.Run()
}

const workspaceReadme = `# {{NAME}} workspace

You will write programs in **{{NAME}}**, a programming language you have not
seen before. Learn it from the reference, then solve the tasks.

- Language reference: ` + "`docs/{{BIN}}-reference.md`" + `
- Toolchain: ` + "`bin/{{BIN}} run FILE.{{EXT}}`" + ` runs a program; ` + "`bin/{{BIN}} check FILE.{{EXT}}`" + ` only checks it.
- Tasks: one file per task in ` + "`tasks/`" + `.
- Put your solution to ` + "`tasks/ID.md`" + ` in ` + "`solutions/ID.{{EXT}}`" + `.

Programs read standard input and write standard output. Your solutions are
graded by running them on hidden test inputs and comparing the output
exactly.
`

func genWorkspace(d *lang.Dialect, seed uint64, semantics, tasksDir, out string, bake bool) error {
	all, err := tasks.Load(tasksDir)
	if err != nil {
		return err
	}
	bin := docs.BinName(d)
	for _, sub := range []string{"docs", "tasks", "solutions", "bin"} {
		if err := os.MkdirAll(filepath.Join(out, sub), 0o755); err != nil {
			return err
		}
	}
	ref, err := docs.Render(d)
	if err != nil {
		return err
	}
	if err := os.WriteFile(filepath.Join(out, "docs", bin+"-reference.md"), []byte(ref), 0o644); err != nil {
		return err
	}
	readme := strings.NewReplacer("{{NAME}}", d.Name, "{{BIN}}", bin, "{{EXT}}", d.Ext).Replace(workspaceReadme)
	if err := os.WriteFile(filepath.Join(out, "README.md"), []byte(readme), 0o644); err != nil {
		return err
	}
	for _, t := range all {
		p, err := t.RenderPrompt(d)
		if err != nil {
			return err
		}
		if err := os.WriteFile(filepath.Join(out, "tasks", t.ID+".md"), []byte(p), 0o644); err != nil {
			return err
		}
	}
	if bake {
		return bakeBinary(seed, semantics, filepath.Join(out, "bin", bin))
	}
	return nil
}
