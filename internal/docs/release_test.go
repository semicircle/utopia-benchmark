package docs

import (
	"encoding/json"
	"os"
	"path/filepath"
	"reflect"
	"testing"

	"utopia/internal/gen"
)

// A published release fixes its languages. If a change to the generator or
// the reference would alter one, this test fails: such a change needs a new
// release, not a silent edit to an old one.
func TestReleasesAreFrozen(t *testing.T) {
	dirs, _ := filepath.Glob("../../releases/*/release.json")
	if len(dirs) == 0 {
		t.Fatal("no releases found")
	}
	for _, path := range dirs {
		var rel struct {
			Semantics string
			Languages []struct {
				Seed      uint64
				Name, Dir string
			}
		}
		raw, err := os.ReadFile(path)
		if err != nil {
			t.Fatal(err)
		}
		if err := json.Unmarshal(raw, &rel); err != nil {
			t.Fatalf("%s: %v", path, err)
		}
		root := filepath.Dir(path)
		for _, l := range rel.Languages {
			d := gen.Generate(gen.Options{Seed: l.Seed, Semantics: gen.SemanticsMode(rel.Semantics)})
			if d.Name != l.Name {
				t.Errorf("%s seed %d: generator now names it %s, release says %s", path, l.Seed, d.Name, l.Name)
			}
			text, err := Render(d)
			if err != nil {
				t.Fatal(err)
			}
			want, err := os.ReadFile(filepath.Join(root, l.Dir, "reference.md"))
			if err != nil {
				t.Fatal(err)
			}
			if text != string(want) {
				t.Errorf("%s: the reference for %s (seed %d) no longer matches the published one", path, l.Name, l.Seed)
			}
			var settings struct{ Semantics map[string]any }
			raw, err := os.ReadFile(filepath.Join(root, l.Dir, "settings.json"))
			if err != nil {
				t.Fatal(err)
			}
			if err := json.Unmarshal(raw, &settings); err != nil {
				t.Fatal(err)
			}
			var got map[string]any
			b, _ := json.Marshal(d.Sem)
			json.Unmarshal(b, &got)
			if !reflect.DeepEqual(got, settings.Semantics) {
				t.Errorf("%s: the semantics of %s (seed %d) changed: %v, published %v", path, l.Name, l.Seed, got, settings.Semantics)
			}
		}
	}
}
