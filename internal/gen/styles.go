package gen

import . "utopia/internal/lang"

// buildShapes assembles the statement templates for a combination of styles.
// Slot names must match what lang's builders expect.
func buildShapes(st Styles, assign string) map[Construct][]Part {
	sh := map[Construct][]Part{
		CLet:         {Kw(RLet), Id("name"), Pu(assign), Ex("value"), Term()},
		CAssign:      {Id("name"), Pu(assign), Ex("value"), Term()},
		CIndexAssign: {Id("name"), Pu("["), Ex("index"), Pu("]"), Pu(assign), Ex("value"), Term()},
		CCallStmt:    {Id("fn"), Pu("("), List("args", ",", 0, Ex("a")), Pu(")"), Term()},
		CPrint:       {Kw(RPrint), Ex("value"), Term()},
		CWrite:       {Kw(RWrite), Ex("value"), Term()},
		CReturn:      {Kw(RReturn), Opt("value", Ex("value")), Term()},
	}
	params := List("params", ",", 0, Id("p"))

	switch st.Func {
	case StyleC, StyleCanon:
		sh[CFunc] = []Part{Kw(RFunc), Id("name"), Pu("("), params, Pu(")"), Pu("{"), Body("body"), Pu("}")}
	case StylePascal:
		sh[CFunc] = []Part{Kw(RFunc), Id("name"), Pu("("), params, Pu(")"), Kw(RBegin), Body("body"), Kw(REnd)}
	case StyleBasic:
		sh[CFunc] = []Part{Kw(RFunc), Id("name"), Pu("("), params, Pu(")"), Body("body"), Kw(REnd), Kw(RFunc)}
	case StyleAsm:
		sh[CFunc] = []Part{Kw(RFunc), Id("name"), Pu("("), params, Pu(")"), Body("body"), Kw(REndFunc)}
	}

	switch st.If {
	case StyleC, StyleCanon:
		sh[CIf] = []Part{Kw(RIf), Pu("("), Ex("cond"), Pu(")"), Pu("{"), Body("then"), Pu("}"),
			Rep("elifs", Kw(RElse), Kw(RIf), Pu("("), Ex("cond"), Pu(")"), Pu("{"), Body("body"), Pu("}")),
			Opt("else", Kw(RElse), Pu("{"), Body("body"), Pu("}"))}
	case StylePascal:
		sh[CIf] = []Part{Kw(RIf), Ex("cond"), Kw(RThen), Kw(RBegin), Body("then"), Kw(REnd),
			Rep("elifs", Kw(RElse), Kw(RIf), Ex("cond"), Kw(RThen), Kw(RBegin), Body("body"), Kw(REnd)),
			Opt("else", Kw(RElse), Kw(RBegin), Body("body"), Kw(REnd))}
	case StyleBasic:
		sh[CIf] = []Part{Kw(RIf), Ex("cond"), Kw(RThen), Body("then"),
			Rep("elifs", Kw(RElseIf), Ex("cond"), Kw(RThen), Body("body")),
			Opt("else", Kw(RElse), Body("body")),
			Kw(REnd), Kw(RIf)}
	}

	values := List("values", ",", 1, Lit("v"))
	switch st.Switch {
	case StyleC, StyleCanon:
		sh[CSwitch] = []Part{Kw(RSwitch), Pu("("), Ex("subject"), Pu(")"), Pu("{"),
			Lines(Rep("cases", Kw(RCase), values, Pu(":"), Body("body"))),
			Lines(Opt("default", Kw(RDefault), Pu(":"), Body("body"))),
			Pu("}")}
	case StylePascal:
		sh[CSwitch] = []Part{Kw(RCase), Ex("subject"), Kw(ROf),
			Lines(Rep("cases", values, Pu(":"), Kw(RBegin), Body("body"), Kw(REnd))),
			Lines(Opt("default", Kw(RElse), Kw(RBegin), Body("body"), Kw(REnd))),
			Kw(REnd)}
	case StyleBasic:
		sh[CSwitch] = []Part{Kw(RSelect), Kw(RCase), Ex("subject"),
			Lines(Rep("cases", Kw(RCase), values, Body("body"))),
			Lines(Opt("default", Kw(RCase), Kw(RElse), Body("body"))),
			Kw(REnd), Kw(RSelect)}
	case StyleAsm:
		sh[CDispatch] = []Part{Kw(RDispatch), Ex("subject"), Pu(":"),
			List("entries", ",", 1, Lit("v"), Pu("->"), Id("label")),
			Opt("else", Kw(RElse), Id("label")), Term()}
	}

	step := Opt("step", Kw(RStep), Ex("step"))
	switch st.Loop {
	case StyleC:
		sh[CWhile] = []Part{Kw(RWhile), Pu("("), Ex("cond"), Pu(")"), Pu("{"), Body("body"), Pu("}")}
		sh[CDoWhile] = []Part{Kw(RDo), Pu("{"), Body("body"), Pu("}"), Kw(RWhile), Pu("("), Ex("cond"), Pu(")"), Term()}
		sh[CCFor] = []Part{Kw(RFor), Pu("("), Simple("init"), Pu(";"), Ex("cond"), Pu(";"), Simple("post"), Pu(")"), Pu("{"), Body("body"), Pu("}")}
	case StylePascal:
		sh[CWhile] = []Part{Kw(RWhile), Ex("cond"), Kw(RDo), Kw(RBegin), Body("body"), Kw(REnd)}
		sh[CRepeatUntil] = []Part{Kw(RRepeat), Body("body"), Kw(RUntil), Ex("cond"), Term()}
		sh[CCountFor] = []Part{Kw(RFor), Id("var"), Pu(assign), Ex("from"), Kw(RTo), Ex("to"), step, Kw(RDo), Kw(RBegin), Body("body"), Kw(REnd)}
	case StyleBasic:
		sh[CWhile] = []Part{Kw(RWhile), Ex("cond"), Body("body"), Kw(RWend)}
		sh[CRepeatUntil] = []Part{Kw(RDo), Body("body"), Kw(RLoop), Kw(RUntil), Ex("cond")}
		sh[CCountFor] = []Part{Kw(RFor), Id("var"), Pu(assign), Ex("from"), Kw(RTo), Ex("to"), step, Body("body"), Kw(RNext), Same("var")}
	case StyleCanon:
		sh[CWhile] = []Part{Kw(RWhile), Pu("("), Ex("cond"), Pu(")"), Pu("{"), Body("body"), Pu("}")}
		sh[CDoWhile] = []Part{Kw(RDo), Pu("{"), Body("body"), Pu("}"), Kw(RWhile), Pu("("), Ex("cond"), Pu(")"), Term()}
		sh[CRepeatUntil] = []Part{Kw(RRepeat), Pu("{"), Body("body"), Pu("}"), Kw(RUntil), Pu("("), Ex("cond"), Pu(")"), Term()}
		sh[CCFor] = []Part{Kw(RFor), Pu("("), Simple("init"), Pu(";"), Ex("cond"), Pu(";"), Simple("post"), Pu(")"), Pu("{"), Body("body"), Pu("}")}
		sh[CCountFor] = []Part{Kw(RCount), Id("var"), Kw(RFrom), Ex("from"), Kw(RTo), Ex("to"), step, Pu("{"), Body("body"), Pu("}")}
	}

	structuredLoops := st.Loop != StyleAsm
	if structuredLoops || st.Switch == StyleC {
		sh[CBreak] = []Part{Kw(RBreak), Term()}
	}
	if structuredLoops {
		sh[CContinue] = []Part{Kw(RContinue), Term()}
	}
	if st.If == StyleAsm || st.Switch == StyleAsm || st.Loop == StyleAsm {
		sh[CLabel] = []Part{Id("label"), Pu(":")}
		sh[CGoto] = []Part{Kw(RGoto), Id("label"), Term()}
		sh[CJumpIf] = []Part{Kw(RJumpIf), Ex("cond"), Pu(","), Id("label"), Term()}
	}
	return sh
}

// alwaysRoles are keywords every dialect has, independent of its shapes.
var alwaysRoles = []Role{RTrue, RFalse, RNone, RAnd, ROr, RNot}
