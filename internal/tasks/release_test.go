package tasks

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"os"
	"path/filepath"
	"sort"
	"testing"
)

// Digest identifies a set of tasks by their prompts and hidden tests, so a
// release can pin exactly what it measured.
func Digest(all []*Task, ids []string) string {
	byID := map[string]*Task{}
	for _, t := range all {
		byID[t.ID] = t
	}
	ids = append([]string(nil), ids...)
	sort.Strings(ids)
	h := sha256.New()
	for _, id := range ids {
		t := byID[id]
		if t == nil {
			h.Write([]byte("== missing " + id + "\n"))
			continue
		}
		h.Write([]byte("== " + id + "\n" + t.Prompt))
		for _, tc := range t.Tests {
			h.Write([]byte("-- " + tc.Name + ".in\n" + tc.Input + "-- " + tc.Name + ".out\n" + tc.Output))
		}
	}
	return hex.EncodeToString(h.Sum(nil))
}

// A published release fixes its tasks: changing a prompt or a hidden test of
// one of them needs a new release, not a silent edit to an old one.
func TestReleaseTasksAreFrozen(t *testing.T) {
	all, err := Load("../../tasks")
	if err != nil {
		t.Fatal(err)
	}
	paths, _ := filepath.Glob("../../releases/*/release.json")
	for _, path := range paths {
		var rel struct {
			Tasks       []string
			TasksSha256 string `json:"tasks_sha256"`
		}
		raw, err := os.ReadFile(path)
		if err != nil {
			t.Fatal(err)
		}
		if err := json.Unmarshal(raw, &rel); err != nil {
			t.Fatalf("%s: %v", path, err)
		}
		if len(rel.Tasks) == 0 {
			t.Errorf("%s: lists no tasks", path)
			continue
		}
		if got := Digest(all, rel.Tasks); got != rel.TasksSha256 {
			t.Errorf("%s: its tasks changed (tasks_sha256 is now %s)", path, got)
		}
	}
}
