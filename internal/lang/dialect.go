package lang

import "sort"

// Role is the meaning of a keyword. Each dialect maps roles to its own words.
type Role string

const (
	RLet      Role = "let"
	RPrint    Role = "print"
	RWrite    Role = "write"
	RReturn   Role = "return"
	RBreak    Role = "break"
	RContinue Role = "continue"
	RFunc     Role = "func"
	REndFunc  Role = "endfunc"
	RIf       Role = "if"
	RThen     Role = "then"
	RElse     Role = "else"
	RElseIf   Role = "elseif"
	RWhile    Role = "while"
	RDo       Role = "do"
	RWend     Role = "wend"
	RFor      Role = "for"
	RCount    Role = "count"
	RFrom     Role = "from"
	RTo       Role = "to"
	RStep     Role = "step"
	RNext     Role = "next"
	RRepeat   Role = "repeat"
	RUntil    Role = "until"
	RLoop     Role = "loop"
	RSwitch   Role = "switch"
	RCase     Role = "case"
	RDefault  Role = "default"
	ROf       Role = "of"
	RSelect   Role = "select"
	RBegin    Role = "begin"
	REnd      Role = "end"
	RGoto     Role = "goto"
	RJumpIf   Role = "jumpif"
	RDispatch Role = "dispatch"
	RTrue     Role = "true"
	RFalse    Role = "false"
	RNone     Role = "none"
	RAnd      Role = "and"
	ROr       Role = "or"
	RNot      Role = "not"
	RMod      Role = "mod"
)

// Construct names a statement form whose syntax is given by a shape.
type Construct string

const (
	CLet         Construct = "let"
	CAssign      Construct = "assign"
	CIndexAssign Construct = "index-assign"
	CCallStmt    Construct = "call"
	CPrint       Construct = "print"
	CWrite       Construct = "write"
	CReturn      Construct = "return"
	CBreak       Construct = "break"
	CContinue    Construct = "continue"
	CLabel       Construct = "label"
	CGoto        Construct = "goto"
	CJumpIf      Construct = "jumpif"
	CIf          Construct = "if"
	CSwitch      Construct = "switch"
	CDispatch    Construct = "dispatch"
	CWhile       Construct = "while"
	CDoWhile     Construct = "do-while"
	CRepeatUntil Construct = "repeat-until"
	CCFor        Construct = "c-for"
	CCountFor    Construct = "count-for"
	CFunc        Construct = "func"
)

// ConstructOrder fixes the order in which shapes are tried and documented.
var ConstructOrder = []Construct{
	CLet, CIndexAssign, CAssign, CCallStmt, CLabel, CPrint, CWrite, CReturn,
	CBreak, CContinue, CGoto, CJumpIf, CIf, CSwitch, CDispatch, CWhile,
	CDoWhile, CRepeatUntil, CCFor, CCountFor, CFunc,
}

// PartKind is one element of a shape template.
type PartKind uint8

const (
	PKw     PartKind = iota // keyword (Role)
	PPunct                  // punctuation or operator (Text)
	PTerm                   // the dialect's statement terminator
	PExpr                   // expression (Slot)
	PIdent                  // identifier (Slot)
	PSame                   // identifier that must equal the one in Slot
	PBody                   // statement list (Slot)
	PSimple                 // let/assign without terminator, may be empty (Slot)
	PLit                    // literal: integer, negative integer or string (Slot)
	POpt                    // optional group (Slot, Sub)
	PRep                    // zero or more groups (Slot, Sub)
	PList                   // Text-separated list of groups (Slot, Sub, Min)
)

type Part struct {
	Kind PartKind
	Role Role
	Text string
	Slot string
	Sub  []Part
	Min  int
	NL   bool // printer starts each group on a new line
}

func Kw(r Role) Part                    { return Part{Kind: PKw, Role: r} }
func Pu(s string) Part                  { return Part{Kind: PPunct, Text: s} }
func Term() Part                        { return Part{Kind: PTerm} }
func Ex(slot string) Part               { return Part{Kind: PExpr, Slot: slot} }
func Id(slot string) Part               { return Part{Kind: PIdent, Slot: slot} }
func Same(slot string) Part             { return Part{Kind: PSame, Slot: slot} }
func Body(slot string) Part             { return Part{Kind: PBody, Slot: slot} }
func Simple(slot string) Part           { return Part{Kind: PSimple, Slot: slot} }
func Lit(slot string) Part              { return Part{Kind: PLit, Slot: slot} }
func Opt(slot string, sub ...Part) Part { return Part{Kind: POpt, Slot: slot, Sub: sub} }
func Rep(slot string, sub ...Part) Part { return Part{Kind: PRep, Slot: slot, Sub: sub} }

// Lines marks an optional or repeated group to start on its own line.
func Lines(p Part) Part { p.NL = true; return p }

func List(slot, sep string, min int, sub ...Part) Part {
	return Part{Kind: PList, Slot: slot, Text: sep, Min: min, Sub: sub}
}

// Style names a family of syntax for one category of constructs.
type Style string

const (
	StyleC      Style = "c"
	StylePascal Style = "pascal"
	StyleBasic  Style = "basic"
	StyleAsm    Style = "asm"
	StyleCanon  Style = "canonical"
)

type Styles struct {
	Func, If, Switch, Loop Style
}

type PrecModel string

const (
	PrecStandard  PrecModel = "standard"   // usual math precedence, left associative
	PrecFlatLeft  PrecModel = "flat-left"  // one level, evaluated left to right (Smalltalk)
	PrecFlatRight PrecModel = "flat-right" // one level, grouped right to left (APL)
)

type Order string

const (
	LeftToRight Order = "left-to-right"
	RightToLeft Order = "right-to-left"
)

type DivMode string

const (
	DivTrunc DivMode = "toward-zero"
	DivFloor DivMode = "toward-negative-infinity"
	DivCeil  DivMode = "toward-positive-infinity"
)

type OORMode string

const (
	OORError OORMode = "error"
	OORWrap  OORMode = "wrap"
)

// Semantics are the behavioral knobs ("false friends") of a dialect.
type Semantics struct {
	ArgOrder          Order
	OperandOrder      Order
	Div               DivMode
	IndexBase         int
	OutOfRange        OORMode
	CountInclusive    bool // upper bound of a counting loop is included
	ShortCircuit      bool
	SwitchFallthrough bool // C-style switch only
	ListEqStructural  bool
	Prec              PrecModel
}

// Ops is the operator spelling of a dialect.
type Ops struct {
	Assign string
	Eq     string
	Ne     string
	Concat string // "+" means concatenation shares the addition operator
	Mod    string // "" means the mod keyword (RMod) is used
}

// Dialect is everything needed to lex, parse, print, compile and document
// programs in one generated language.
type Dialect struct {
	Name       string
	Ext        string
	Seed       uint64
	Keywords   map[Role]string
	Builtins   map[Builtin]string
	Ops        Ops
	Terminator string
	Comment    string
	Styles     Styles
	Shapes     map[Construct][]Part
	Sem        Semantics
}

// Word returns the dialect's word for a role.
func (d *Dialect) Word(r Role) string { return d.Keywords[r] }

// Has reports whether the dialect has syntax for a construct.
func (d *Dialect) Has(c Construct) bool { _, ok := d.Shapes[c]; return ok }

// UsedRoles returns the roles the dialect uses, sorted.
func (d *Dialect) UsedRoles() []Role {
	rs := make([]Role, 0, len(d.Keywords))
	for r := range d.Keywords {
		rs = append(rs, r)
	}
	sort.Slice(rs, func(i, j int) bool { return rs[i] < rs[j] })
	return rs
}

// ShapeRoles collects every keyword role referenced by the given parts.
func ShapeRoles(parts []Part, into map[Role]bool) {
	for _, p := range parts {
		if p.Kind == PKw {
			into[p.Role] = true
		}
		ShapeRoles(p.Sub, into)
	}
}
