package vm

import (
	"strconv"
	"strings"

	. "utopia/internal/lang"
)

type Kind uint8

const (
	KUnset Kind = iota
	KNone
	KInt
	KStr
	KBool
	KList
)

type ListObj struct{ Elems []Value }

type Value struct {
	K Kind
	I int64
	S string
	L *ListObj
}

func IntVal(i int64) Value  { return Value{K: KInt, I: i} }
func StrVal(s string) Value { return Value{K: KStr, S: s} }
func NoneVal() Value        { return Value{K: KNone} }
func BoolVal(b bool) Value {
	if b {
		return Value{K: KBool, I: 1}
	}
	return Value{K: KBool}
}

// typeName is the dialect-neutral English name used in error messages.
func typeName(v Value) string {
	switch v.K {
	case KNone:
		return "none"
	case KInt:
		return "integer"
	case KStr:
		return "string"
	case KBool:
		return "boolean"
	case KList:
		return "list"
	}
	return "unset"
}

// display renders a value the way print shows it.
func display(d *Dialect, v Value, nested bool) string {
	switch v.K {
	case KNone:
		return d.Word(RNone)
	case KInt:
		return strconv.FormatInt(v.I, 10)
	case KStr:
		if nested {
			return QuoteString(v.S)
		}
		return v.S
	case KBool:
		if v.I != 0 {
			return d.Word(RTrue)
		}
		return d.Word(RFalse)
	case KList:
		parts := make([]string, len(v.L.Elems))
		for i, e := range v.L.Elems {
			parts[i] = display(d, e, true)
		}
		return "[" + strings.Join(parts, ", ") + "]"
	}
	return "?"
}

func equal(structural bool, a, b Value) bool {
	if a.K != b.K {
		return false
	}
	switch a.K {
	case KNone:
		return true
	case KInt, KBool:
		return a.I == b.I
	case KStr:
		return a.S == b.S
	case KList:
		if a.L == b.L {
			return true
		}
		if !structural || len(a.L.Elems) != len(b.L.Elems) {
			return false
		}
		for i := range a.L.Elems {
			if !equal(structural, a.L.Elems[i], b.L.Elems[i]) {
				return false
			}
		}
		return true
	}
	return false
}
