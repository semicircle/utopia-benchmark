// Package gen generates a complete dialect from a seed.
package gen

import (
	"math/rand/v2"
	"sort"
	"strings"

	. "utopia/internal/lang"
)

// SemanticsMode selects how behavioral knobs are chosen.
type SemanticsMode string

const (
	SemRandom   SemanticsMode = "random"   // false friends drawn from the seed
	SemStandard SemanticsMode = "standard" // conventional behavior; syntax-only novelty
)

type Options struct {
	Seed      uint64
	Semantics SemanticsMode
}

type weighted[T any] struct {
	v T
	w int
}

func pick[T any](r *rand.Rand, opts ...weighted[T]) T {
	total := 0
	for _, o := range opts {
		total += o.w
	}
	n := r.IntN(total)
	for _, o := range opts {
		if n < o.w {
			return o.v
		}
		n -= o.w
	}
	return opts[len(opts)-1].v
}

func w[T any](v T, weight int) weighted[T] { return weighted[T]{v, weight} }

func chance(r *rand.Rand, p float64) bool { return r.Float64() < p }

// StandardSemantics is conventional, mainstream behavior.
func StandardSemantics() Semantics {
	return Semantics{
		ArgOrder: LeftToRight, OperandOrder: LeftToRight, Div: DivTrunc,
		IndexBase: 0, OutOfRange: OORError, CountInclusive: true,
		ShortCircuit: true, SwitchFallthrough: false, ListEqStructural: true,
		Prec: PrecStandard,
	}
}

// Generate builds the dialect for a seed. The same seed and generator version
// always give the same dialect.
func Generate(opt Options) *Dialect {
	r := rand.New(rand.NewPCG(opt.Seed, 0x75746f706961))

	structured := func() Style {
		return pick(r, w(StyleC, 3), w(StylePascal, 3), w(StyleBasic, 3), w(StyleAsm, 1))
	}
	st := Styles{
		Func:   pick(r, w(StyleC, 1), w(StylePascal, 1), w(StyleBasic, 1), w(StyleAsm, 1)),
		If:     structured(),
		Switch: structured(),
		Loop:   structured(),
	}

	var ops Ops
	ops.Assign = pick(r, w("=", 2), w(":=", 2), w("<-", 1))
	if ops.Assign == "=" {
		ops.Eq = "=="
	} else {
		ops.Eq = pick(r, w("=", 1), w("==", 1))
	}
	ops.Ne = pick(r, w("!=", 2), w("<>", 2), w("/=", 1), w("~=", 1))
	term := pick(r, w(";", 7), w(".", 3))
	concats := []weighted[string]{w("+", 2), w("&", 2), w("++", 1)}
	if term != "." {
		concats = append(concats, w("..", 1))
	}
	ops.Concat = pick(r, concats...)
	if chance(r, 0.5) {
		ops.Mod = "%"
	}
	comments := []weighted[string]{w("#", 3), w("//", 3), w("--", 1), w("'", 1)}
	if term != ";" && st.Loop != StyleC {
		comments = append(comments, w(";", 1))
	}
	comment := pick(r, comments...)

	sem := StandardSemantics()
	// Draw every knob even in standard mode, so the random stream (and thus
	// the lexicon) is the same for a seed in both modes.
	rs := Semantics{
		ArgOrder:          pick(r, w(LeftToRight, 1), w(RightToLeft, 1)),
		OperandOrder:      pick(r, w(LeftToRight, 7), w(RightToLeft, 3)),
		Div:               pick(r, w(DivTrunc, 1), w(DivFloor, 1), w(DivCeil, 1)),
		IndexBase:         pick(r, w(0, 1), w(1, 1)),
		OutOfRange:        pick(r, w(OORError, 3), w(OORWrap, 2)),
		CountInclusive:    chance(r, 0.5),
		ShortCircuit:      chance(r, 0.7),
		SwitchFallthrough: chance(r, 0.5),
		ListEqStructural:  chance(r, 0.5),
		Prec:              pick(r, w(PrecStandard, 2), w(PrecFlatLeft, 1), w(PrecFlatRight, 1)),
	}
	if opt.Semantics != SemStandard {
		sem = rs
	}

	shapes := buildShapes(st, ops.Assign)
	roleSet := map[Role]bool{}
	for _, s := range shapes {
		ShapeRoles(s, roleSet)
	}
	for _, rl := range alwaysRoles {
		roleSet[rl] = true
	}
	if ops.Mod == "" {
		roleSet[RMod] = true
	}
	roles := make([]Role, 0, len(roleSet))
	for rl := range roleSet {
		roles = append(roles, rl)
	}
	sort.Slice(roles, func(i, j int) bool { return roles[i] < roles[j] })

	lx := newLexicon(r)
	name := lx.fresh(5, 9)
	caseFn := pick(r, w(strings.ToLower, 6), w(strings.ToUpper, 2), w(titleCase, 2))
	kw := map[Role]string{}
	for _, rl := range roles {
		kw[rl] = caseFn(lx.fresh(3, 8))
	}
	bi := map[Builtin]string{}
	for _, b := range AllBuiltins {
		bi[b] = caseFn(lx.fresh(3, 9))
	}

	ext := name
	if len(ext) > 3 {
		ext = ext[:3]
	}
	return &Dialect{
		Name: titleCase(name), Ext: ext, Seed: opt.Seed,
		Keywords: kw, Builtins: bi, Ops: ops, Terminator: term, Comment: comment,
		Styles: st, Shapes: shapes, Sem: sem,
	}
}

func titleCase(s string) string {
	if s == "" {
		return s
	}
	return strings.ToUpper(s[:1]) + s[1:]
}

// Canonical is the fixed, English-keyword dialect that task solutions and
// documentation examples are written in. It can express every construct.
func Canonical() *Dialect {
	st := Styles{Func: StyleCanon, If: StyleCanon, Switch: StyleCanon, Loop: StyleCanon}
	ops := Ops{Assign: "=", Eq: "==", Ne: "!=", Concat: "&", Mod: "%"}
	shapes := buildShapes(st, ops.Assign)
	roleSet := map[Role]bool{}
	for _, s := range shapes {
		ShapeRoles(s, roleSet)
	}
	for _, rl := range alwaysRoles {
		roleSet[rl] = true
	}
	kw := map[Role]string{}
	for rl := range roleSet {
		kw[rl] = string(rl)
	}
	return &Dialect{
		Name: "Canonical", Ext: "canon",
		Keywords: kw,
		Builtins: map[Builtin]string{BLen: "len", BPush: "push", BStr: "str", BNum: "num", BReadline: "readline"},
		Ops:      ops, Terminator: ";", Comment: "#",
		Styles: st, Shapes: shapes, Sem: StandardSemantics(),
	}
}
