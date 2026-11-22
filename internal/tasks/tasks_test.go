package tasks

import (
	"os"
	"strings"
	"testing"

	"utopia/internal/gen"
	"utopia/internal/lang"
	"utopia/internal/lower"
	"utopia/internal/vm"
)

// Every reference solution must pass its tests in the canonical dialect and
// in many generated dialects, both with random and standard semantics.
func TestReferenceSolutionsAcrossDialects(t *testing.T) {
	all, err := Load("../../tasks")
	if err != nil {
		t.Fatal(err)
	}
	dialects := []*lang.Dialect{gen.Canonical()}
	for seed := uint64(1); seed <= 300; seed++ {
		dialects = append(dialects,
			gen.Generate(gen.Options{Seed: seed}),
			gen.Generate(gen.Options{Seed: seed, Semantics: gen.SemStandard}))
	}
	for _, task := range all {
		task := task
		t.Run(task.ID, func(t *testing.T) {
			t.Parallel()
			for _, d := range dialects {
				src, err := task.RenderSolution(d)
				if err != nil {
					t.Fatalf("seed %d: %v", d.Seed, err)
				}
				for _, tc := range task.Tests {
					var out strings.Builder
					err := vm.RunSource(d, src, vm.Options{Stdin: strings.NewReader(tc.Input), Stdout: &out})
					if err != nil || out.String() != tc.Output {
						t.Fatalf("%s/%s seed %d (%s): err=%v\n--- want ---\n%s--- got ---\n%s--- source ---\n%s",
							task.ID, tc.Name, d.Seed, d.Name, err, tc.Output, out.String(), src)
					}
				}
			}
		})
	}
}

// TestHabitTraps reports, per task, how often a solution written by habit
// fails: the reference translated into each dialect without compensating
// for its semantics (index base, loop bounds, fallthrough, division). A
// task whose rate is near zero has no trap. It is slow, so it runs only
// when asked: UTOPIA_TRAPS=1 go test ./internal/tasks -run HabitTraps -v
func TestHabitTraps(t *testing.T) {
	if os.Getenv("UTOPIA_TRAPS") == "" {
		t.Skip("set UTOPIA_TRAPS=1 to run")
	}
	all, err := Load("../../tasks")
	if err != nil {
		t.Fatal(err)
	}
	const seeds = 200
	for _, task := range all {
		prog, err := lang.Parse(gen.Canonical(), task.Solution)
		if err != nil {
			t.Fatal(err)
		}
		failed := 0
		for seed := uint64(1); seed <= seeds; seed++ {
			d := gen.Generate(gen.Options{Seed: seed})
			low, err := lower.Lower(d, prog, lower.Options{Raw: true})
			if err != nil {
				t.Fatal(err)
			}
			src := lang.Format(d, low)
			for _, tc := range task.Tests {
				var out strings.Builder
				err := vm.RunSource(d, src, vm.Options{Stdin: strings.NewReader(tc.Input), Stdout: &out})
				if err != nil || out.String() != tc.Output {
					failed++
					break
				}
			}
		}
		t.Logf("%-18s habit-written solution fails in %3d%% of dialects", task.ID, 100*failed/seeds)
	}
}
