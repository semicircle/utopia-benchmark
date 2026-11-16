package tasks

import (
	"strings"
	"testing"

	"utopia/internal/gen"
	"utopia/internal/lang"
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
	}
}
