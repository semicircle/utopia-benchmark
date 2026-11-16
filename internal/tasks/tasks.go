// Package tasks loads benchmark tasks. A task is a directory holding
// task.md (the prompt, a template), solution.canon (a reference solution in
// the canonical dialect) and tests/NN.in / tests/NN.out pairs.
package tasks

import (
	"bytes"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"text/template"

	"utopia/internal/gen"
	"utopia/internal/lang"
	"utopia/internal/lower"
)

type Test struct {
	Name   string
	Input  string
	Output string
}

type Task struct {
	ID       string
	Prompt   string // template text
	Solution string // canonical source
	Tests    []Test
}

// Load reads every task directory under root, sorted by ID.
func Load(root string) ([]*Task, error) {
	entries, err := os.ReadDir(root)
	if err != nil {
		return nil, err
	}
	var out []*Task
	for _, e := range entries {
		if !e.IsDir() {
			continue
		}
		t, err := LoadOne(filepath.Join(root, e.Name()))
		if err != nil {
			return nil, err
		}
		out = append(out, t)
	}
	sort.Slice(out, func(i, j int) bool { return out[i].ID < out[j].ID })
	return out, nil
}

func LoadOne(dir string) (*Task, error) {
	prompt, err := os.ReadFile(filepath.Join(dir, "task.md"))
	if err != nil {
		return nil, err
	}
	sol, err := os.ReadFile(filepath.Join(dir, "solution.canon"))
	if err != nil {
		return nil, err
	}
	t := &Task{ID: filepath.Base(dir), Prompt: string(prompt), Solution: string(sol)}
	outs, err := filepath.Glob(filepath.Join(dir, "tests", "*.out"))
	if err != nil {
		return nil, err
	}
	sort.Strings(outs)
	for _, o := range outs {
		want, err := os.ReadFile(o)
		if err != nil {
			return nil, err
		}
		base := strings.TrimSuffix(o, ".out")
		in, err := os.ReadFile(base + ".in")
		if err != nil && !os.IsNotExist(err) {
			return nil, err
		}
		t.Tests = append(t.Tests, Test{Name: filepath.Base(base), Input: string(in), Output: string(want)})
	}
	if len(t.Tests) == 0 {
		return nil, fmt.Errorf("task %s has no tests", t.ID)
	}
	return t, nil
}

// RenderPrompt fills in the task prompt for a dialect.
func (t *Task) RenderPrompt(d *lang.Dialect) (string, error) {
	tmpl, err := template.New(t.ID).Parse(t.Prompt)
	if err != nil {
		return "", err
	}
	var buf bytes.Buffer
	err = tmpl.Execute(&buf, map[string]string{"Lang": d.Name, "Ext": d.Ext})
	return buf.String(), err
}

// RenderSolution translates the reference solution into dialect d.
func (t *Task) RenderSolution(d *lang.Dialect) (string, error) {
	prog, err := lang.Parse(gen.Canonical(), t.Solution)
	if err != nil {
		return "", fmt.Errorf("%s: solution: %w", t.ID, err)
	}
	low, err := lower.Lower(d, prog, lower.Options{})
	if err != nil {
		return "", fmt.Errorf("%s: %w", t.ID, err)
	}
	return lang.Format(d, low), nil
}
