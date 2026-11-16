package gen

import (
	"math/rand/v2"
	"strings"
)

// phonology is a small random sound system, so each dialect's words share a
// consistent "feel" but no dialect looks like a human language.
type phonology struct {
	onsets []string
	vowels []string
	codas  []string
	codaP  float64 // chance a syllable is closed
	minSyl int
	maxSyl int
}

var (
	allOnsets = []string{"p", "t", "k", "b", "d", "g", "m", "n", "s", "z", "f", "v", "l", "r", "h", "y", "w", "sh", "ch", "th", "kr", "tr", "pl", "dr"}
	allVowels = []string{"a", "e", "i", "o", "u", "ai", "ou", "ei"}
	allCodas  = []string{"n", "m", "l", "r", "s", "k", "t", "x", "sh"}
)

func pickN(r *rand.Rand, pool []string, lo, hi int) []string {
	p := append([]string(nil), pool...)
	r.Shuffle(len(p), func(i, j int) { p[i], p[j] = p[j], p[i] })
	return p[:lo+r.IntN(hi-lo+1)]
}

func newPhonology(r *rand.Rand) phonology {
	return phonology{
		onsets: pickN(r, allOnsets, 8, 13),
		// Always keep at least three plain vowels so words stay readable.
		vowels: append(pickN(r, allVowels[:5], 3, 5), pickN(r, allVowels[5:], 0, 1)...),
		codas:  pickN(r, allCodas, 2, 5),
		codaP:  0.15 + r.Float64()*0.3,
		minSyl: 1,
		maxSyl: 3,
	}
}

func (ph phonology) word(r *rand.Rand) string {
	n := ph.minSyl + r.IntN(ph.maxSyl-ph.minSyl+1)
	var sb strings.Builder
	for i := 0; i < n; i++ {
		if i > 0 || r.Float64() < 0.85 {
			sb.WriteString(ph.onsets[r.IntN(len(ph.onsets))])
		}
		sb.WriteString(ph.vowels[r.IntN(len(ph.vowels))])
		if r.Float64() < ph.codaP {
			sb.WriteString(ph.codas[r.IntN(len(ph.codas))])
		}
	}
	return sb.String()
}

// blocked words carry meaning from existing programming languages or English.
var blocked = map[string]bool{}

func init() {
	for _, w := range strings.Fields(`
		and or not xor if then else elif elsif elseif endif fi for foreach to downto step next
		while wend do done loop until repeat break continue exit return yield goto go
		func function fun fn def defn sub proc procedure lambda let var val const static
		int integer str string bool boolean char byte long short float double real num number
		true false nil null none nothing void undefined self this new delete del
		case switch select default of when match begin end class struct enum type record
		print printf puts echo write writeln read readln input output len length size push
		pop append list array map set dict table range in is as at by on off with from
		try catch throw raise finally import export module package use let mod div rem
		pass loop label jump jmp call ret halt nop mov add sub mul cmp test inc dec
		the be are was were has had have can will shall may must you she her him his
		its our out all any one two six ten not but yes no ok go see say get put run
		end top bot new old big bad sad mad dad mom man men boy kid god die kill sex ass
		shit fuck damn hell nazi rape cum tit fag nig neg`) {
		blocked[w] = true
	}
}

// lexicon generates distinct, pronounceable words.
type lexicon struct {
	r     *rand.Rand
	ph    phonology
	used  map[string]bool
	lower bool
}

func newLexicon(r *rand.Rand) *lexicon {
	return &lexicon{r: r, ph: newPhonology(r), used: map[string]bool{}}
}

func (lx *lexicon) fresh(minLen, maxLen int) string {
	for {
		w := lx.ph.word(lx.r)
		if len(w) < minLen || len(w) > maxLen || blocked[w] || lx.used[w] {
			continue
		}
		bad := false
		for b := range blocked {
			// Avoid words that merely add a letter to a well-known keyword.
			if len(b) >= 4 && strings.Contains(w, b) {
				bad = true
				break
			}
		}
		if bad {
			continue
		}
		// Keep every word at least two edits away from the others, so no two
		// keywords differ by a single letter.
		for u := range lx.used {
			if editDistance(u, w) < 2 {
				bad = true
				break
			}
		}
		if bad {
			continue
		}
		lx.used[w] = true
		return w
	}
}

func editDistance(a, b string) int {
	prev := make([]int, len(b)+1)
	cur := make([]int, len(b)+1)
	for j := range prev {
		prev[j] = j
	}
	for i := 1; i <= len(a); i++ {
		cur[0] = i
		for j := 1; j <= len(b); j++ {
			cost := 1
			if a[i-1] == b[j-1] {
				cost = 0
			}
			cur[j] = min(prev[j]+1, cur[j-1]+1, prev[j-1]+cost)
		}
		prev, cur = cur, prev
	}
	return prev[len(b)]
}
