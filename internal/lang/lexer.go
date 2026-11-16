package lang

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

type TokKind uint8

const (
	TEOF TokKind = iota
	TInt
	TStr
	TIdent
	TKw
	TPunct
)

type Token struct {
	Kind TokKind
	Text string // source text (for TStr, the decoded value)
	Role Role   // for TKw
	Int  int64
	Line int
	Col  int
}

// Error is a compile-time error with a source position.
type Error struct {
	Line, Col int
	Msg       string
}

func (e *Error) Error() string {
	if e.Col > 0 {
		return fmt.Sprintf("line %d, column %d: %s", e.Line, e.Col, e.Msg)
	}
	return fmt.Sprintf("line %d: %s", e.Line, e.Msg)
}

// Puncts returns the punctuation and operator tokens of a dialect, longest
// first, so the lexer can use maximal munch.
func (d *Dialect) Puncts() []string {
	set := map[string]bool{}
	for _, p := range []string{"(", ")", "[", "]", "{", "}", ",", ":", ";", "+", "-", "*", "/", "<", ">", "<=", ">=", "->"} {
		set[p] = true
	}
	for _, p := range []string{d.Ops.Assign, d.Ops.Eq, d.Ops.Ne, d.Ops.Concat, d.Ops.Mod, d.Terminator} {
		if p != "" {
			set[p] = true
		}
	}
	out := make([]string, 0, len(set))
	for p := range set {
		out = append(out, p)
	}
	sort.Slice(out, func(i, j int) bool {
		if len(out[i]) != len(out[j]) {
			return len(out[i]) > len(out[j])
		}
		return out[i] < out[j]
	})
	return out
}

// Lex splits source into tokens.
func Lex(d *Dialect, src string) ([]Token, error) {
	words := map[string]Role{}
	for r, w := range d.Keywords {
		words[w] = r
	}
	puncts := d.Puncts()
	var toks []Token
	line, col := 1, 1
	i := 0
	adv := func(n int) {
		for k := 0; k < n; k++ {
			if src[i] == '\n' {
				line++
				col = 1
			} else {
				col++
			}
			i++
		}
	}
	for i < len(src) {
		c := src[i]
		if c == ' ' || c == '\t' || c == '\r' || c == '\n' {
			adv(1)
			continue
		}
		if d.Comment != "" && strings.HasPrefix(src[i:], d.Comment) {
			for i < len(src) && src[i] != '\n' {
				adv(1)
			}
			continue
		}
		startLine, startCol := line, col
		switch {
		case isLetter(c):
			j := i
			for j < len(src) && (isLetter(src[j]) || isDigit(src[j])) {
				j++
			}
			w := src[i:j]
			if r, ok := words[w]; ok {
				toks = append(toks, Token{Kind: TKw, Text: w, Role: r, Line: startLine, Col: startCol})
			} else {
				toks = append(toks, Token{Kind: TIdent, Text: w, Line: startLine, Col: startCol})
			}
			adv(j - i)
		case isDigit(c):
			j := i
			for j < len(src) && isDigit(src[j]) {
				j++
			}
			if j < len(src) && isLetter(src[j]) {
				return nil, &Error{startLine, startCol, fmt.Sprintf("invalid number %q", src[i:j+1])}
			}
			v, err := strconv.ParseInt(src[i:j], 10, 64)
			if err != nil {
				return nil, &Error{startLine, startCol, fmt.Sprintf("integer %s is too large", src[i:j])}
			}
			toks = append(toks, Token{Kind: TInt, Text: src[i:j], Int: v, Line: startLine, Col: startCol})
			adv(j - i)
		case c == '"':
			var sb strings.Builder
			adv(1)
			for {
				if i >= len(src) || src[i] == '\n' {
					return nil, &Error{startLine, startCol, "unterminated string"}
				}
				ch := src[i]
				if ch == '"' {
					adv(1)
					break
				}
				if ch == '\\' {
					if i+1 >= len(src) {
						return nil, &Error{startLine, startCol, "unterminated string"}
					}
					switch src[i+1] {
					case 'n':
						sb.WriteByte('\n')
					case 't':
						sb.WriteByte('\t')
					case '"':
						sb.WriteByte('"')
					case '\\':
						sb.WriteByte('\\')
					default:
						return nil, &Error{line, col, fmt.Sprintf("unknown escape \\%c", src[i+1])}
					}
					adv(2)
					continue
				}
				sb.WriteByte(ch)
				adv(1)
			}
			toks = append(toks, Token{Kind: TStr, Text: sb.String(), Line: startLine, Col: startCol})
		default:
			matched := ""
			for _, p := range puncts {
				if strings.HasPrefix(src[i:], p) {
					matched = p
					break
				}
			}
			if matched == "" {
				return nil, &Error{startLine, startCol, fmt.Sprintf("unexpected character %q", c)}
			}
			toks = append(toks, Token{Kind: TPunct, Text: matched, Line: startLine, Col: startCol})
			adv(len(matched))
		}
	}
	toks = append(toks, Token{Kind: TEOF, Line: line, Col: col})
	return toks, nil
}

func isLetter(c byte) bool { return c == '_' || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') }
func isDigit(c byte) bool  { return c >= '0' && c <= '9' }

// QuoteString renders a string literal in source form.
func QuoteString(s string) string {
	var sb strings.Builder
	sb.WriteByte('"')
	for i := 0; i < len(s); i++ {
		switch s[i] {
		case '\n':
			sb.WriteString(`\n`)
		case '\t':
			sb.WriteString(`\t`)
		case '"':
			sb.WriteString(`\"`)
		case '\\':
			sb.WriteString(`\\`)
		default:
			sb.WriteByte(s[i])
		}
	}
	sb.WriteByte('"')
	return sb.String()
}
