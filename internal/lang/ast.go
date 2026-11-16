// Package lang holds the dialect-independent core of Utopia: the AST, the
// Dialect description, and a lexer, parser and printer that are all driven by
// a dialect's shape templates.
package lang

// ---- Expressions ----

type Expr interface{ exprNode() }

type IntLit struct{ V int64 }
type StrLit struct{ V string }
type BoolLit struct{ V bool }
type NoneLit struct{}
type ListLit struct{ Elems []Expr }
type Ident struct {
	Name string
	Line int
}
type Unary struct {
	Op UnOp
	X  Expr
}
type Binary struct {
	Op   BinOp
	L, R Expr
	Line int
}

// Call is a call to a user function or, when Builtin != BNone, a builtin.
type Call struct {
	Name    string
	Builtin Builtin
	Args    []Expr
	Line    int
}
type Index struct {
	X, I Expr
	Line int
}

func (*IntLit) exprNode()  {}
func (*StrLit) exprNode()  {}
func (*BoolLit) exprNode() {}
func (*NoneLit) exprNode() {}
func (*ListLit) exprNode() {}
func (*Ident) exprNode()   {}
func (*Unary) exprNode()   {}
func (*Binary) exprNode()  {}
func (*Call) exprNode()    {}
func (*Index) exprNode()   {}

type UnOp uint8

const (
	UNeg UnOp = iota
	UNot
)

type BinOp uint8

const (
	BAdd BinOp = iota
	BSub
	BMul
	BDiv
	BMod
	BConcat
	BEq
	BNe
	BLt
	BLe
	BGt
	BGe
	BAnd
	BOr
)

var binOpNames = [...]string{"+", "-", "*", "/", "mod", "concat", "==", "!=", "<", "<=", ">", ">=", "and", "or"}

func (o BinOp) String() string { return binOpNames[o] }

type Builtin uint8

const (
	BNone Builtin = iota
	BLen
	BPush
	BStr
	BNum
	BReadline
)

// AllBuiltins lists the builtins in a fixed order.
var AllBuiltins = []Builtin{BLen, BPush, BStr, BNum, BReadline}

// BuiltinArity is the number of arguments each builtin takes.
var BuiltinArity = map[Builtin]int{BLen: 1, BPush: 2, BStr: 1, BNum: 1, BReadline: 0}

// ---- Statements ----

type Stmt interface{ stmtNode() }

type Let struct {
	Name  string
	Value Expr
	Line  int
}
type Assign struct {
	Name  string
	Value Expr
	Line  int
}
type IndexAssign struct {
	Name         string
	Index, Value Expr
	Line         int
}
type CallStmt struct{ Call *Call }
type Print struct {
	Value   Expr
	Newline bool // false for the "write" statement
	Line    int
}
type Return struct {
	Value Expr // nil for a bare return
	Line  int
}
type Break struct{ Line int }
type Continue struct{ Line int }

type CondArm struct {
	Cond Expr
	Body []Stmt
}
type If struct {
	Arms    []CondArm
	Else    []Stmt
	HasElse bool
	Line    int
}

type Case struct {
	Values []Expr // literals
	Body   []Stmt
}
type Switch struct {
	Subject    Expr
	Cases      []Case
	Default    []Stmt
	HasDefault bool
	Line       int
}

type While struct {
	Cond Expr
	Body []Stmt
	Line int
}

// DoWhile runs Body, then repeats while Cond is true.
type DoWhile struct {
	Body []Stmt
	Cond Expr
	Line int
}

// RepeatUntil runs Body, then repeats until Cond is true.
type RepeatUntil struct {
	Body []Stmt
	Cond Expr
	Line int
}

// CFor is the C-style three-part loop. Init and Post may be nil.
type CFor struct {
	Init Stmt
	Cond Expr
	Post Stmt
	Body []Stmt
	Line int
}

// CountFor counts Var from From to To by Step (nil means 1).
type CountFor struct {
	Var      string
	From, To Expr
	Step     Expr
	Body     []Stmt
	Line     int
}

type Label struct {
	Name string
	Line int
}
type Goto struct {
	Label string
	Line  int
}
type JumpIf struct {
	Cond  Expr
	Label string
	Line  int
}

type DispatchEntry struct {
	Value Expr
	Label string
}
type Dispatch struct {
	Subject Expr
	Entries []DispatchEntry
	Else    string // "" when absent
	Line    int
}

func (*Let) stmtNode()         {}
func (*Assign) stmtNode()      {}
func (*IndexAssign) stmtNode() {}
func (*CallStmt) stmtNode()    {}
func (*Print) stmtNode()       {}
func (*Return) stmtNode()      {}
func (*Break) stmtNode()       {}
func (*Continue) stmtNode()    {}
func (*If) stmtNode()          {}
func (*Switch) stmtNode()      {}
func (*While) stmtNode()       {}
func (*DoWhile) stmtNode()     {}
func (*RepeatUntil) stmtNode() {}
func (*CFor) stmtNode()        {}
func (*CountFor) stmtNode()    {}
func (*Label) stmtNode()       {}
func (*Goto) stmtNode()        {}
func (*JumpIf) stmtNode()      {}
func (*Dispatch) stmtNode()    {}

type FuncDecl struct {
	Name   string
	Params []string
	Body   []Stmt
	Line   int
}

// Program is a whole source file: function declarations plus top-level
// statements, which form the main program.
type Program struct {
	Funcs []*FuncDecl
	Main  []Stmt
}
