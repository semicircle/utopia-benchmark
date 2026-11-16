package docs

import (
	"strings"
	"testing"

	"utopia/internal/gen"
)

// The reference must render for every dialect, with no template holes.
func TestRenderManySeeds(t *testing.T) {
	for seed := uint64(1); seed <= 300; seed++ {
		for _, mode := range []gen.SemanticsMode{gen.SemRandom, gen.SemStandard} {
			d := gen.Generate(gen.Options{Seed: seed, Semantics: mode})
			text, err := Render(d)
			if err != nil {
				t.Fatalf("seed %d %s: %v", seed, mode, err)
			}
			for _, bad := range []string{"<no value>", "%!", "map[", "panic"} {
				if strings.Contains(text, bad) {
					t.Fatalf("seed %d %s: reference contains %q", seed, mode, bad)
				}
			}
		}
	}
}
