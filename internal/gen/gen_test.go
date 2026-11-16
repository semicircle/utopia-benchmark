package gen

import (
	"reflect"
	"testing"

	"utopia/internal/lang"
)

func TestDeterministic(t *testing.T) {
	for seed := uint64(1); seed <= 50; seed++ {
		a := Generate(Options{Seed: seed})
		b := Generate(Options{Seed: seed})
		if !reflect.DeepEqual(a, b) {
			t.Fatalf("seed %d: two generations differ", seed)
		}
		s := Generate(Options{Seed: seed, Semantics: SemStandard})
		if !reflect.DeepEqual(a.Keywords, s.Keywords) || a.Styles != s.Styles {
			t.Fatalf("seed %d: standard semantics changed the syntax", seed)
		}
		if s.Sem != StandardSemantics() {
			t.Fatalf("seed %d: standard mode has non-standard semantics", seed)
		}
	}
}

func TestWordsDistinct(t *testing.T) {
	for seed := uint64(1); seed <= 500; seed++ {
		d := Generate(Options{Seed: seed})
		seen := map[string]bool{d.Name: true}
		var words []string
		for _, r := range d.UsedRoles() {
			words = append(words, d.Keywords[r])
		}
		for _, b := range lang.AllBuiltins {
			words = append(words, d.Builtins[b])
		}
		for _, w := range words {
			if seen[w] {
				t.Fatalf("seed %d: word %q used twice", seed, w)
			}
			seen[w] = true
		}
		for i := range words {
			for j := i + 1; j < len(words); j++ {
				if editDistance(words[i], words[j]) < 2 {
					t.Fatalf("seed %d: %q and %q are too similar", seed, words[i], words[j])
				}
			}
		}
	}
}
