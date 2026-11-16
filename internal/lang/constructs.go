package lang

// This file converts between shape matches and AST nodes. Every style must
// use the slot names below for a construct, so one builder serves them all.

func buildFunc(m *Match) *FuncDecl {
	f := &FuncDecl{Name: m.I["name"], Line: m.Line}
	for _, g := range m.G["params"] {
		f.Params = append(f.Params, g.I["p"])
	}
	f.Body = m.B["body"]
	return f
}

func buildStmt(c Construct, m *Match) Stmt {
	switch c {
	case CLet:
		return &Let{Name: m.I["name"], Value: m.E["value"], Line: m.Line}
	case CAssign:
		return &Assign{Name: m.I["name"], Value: m.E["value"], Line: m.Line}
	case CIndexAssign:
		return &IndexAssign{Name: m.I["name"], Index: m.E["index"], Value: m.E["value"], Line: m.Line}
	case CCallStmt:
		call := &Call{Name: m.I["fn"], Line: m.Line}
		for _, g := range m.G["args"] {
			call.Args = append(call.Args, g.E["a"])
		}
		return &CallStmt{Call: call}
	case CPrint:
		return &Print{Value: m.E["value"], Newline: true, Line: m.Line}
	case CWrite:
		return &Print{Value: m.E["value"], Newline: false, Line: m.Line}
	case CReturn:
		r := &Return{Line: m.Line}
		if g := m.G["value"]; len(g) > 0 {
			r.Value = g[0].E["value"]
		}
		return r
	case CBreak:
		return &Break{Line: m.Line}
	case CContinue:
		return &Continue{Line: m.Line}
	case CLabel:
		return &Label{Name: m.I["label"], Line: m.Line}
	case CGoto:
		return &Goto{Label: m.I["label"], Line: m.Line}
	case CJumpIf:
		return &JumpIf{Cond: m.E["cond"], Label: m.I["label"], Line: m.Line}
	case CIf:
		s := &If{Line: m.Line}
		s.Arms = append(s.Arms, CondArm{Cond: m.E["cond"], Body: m.B["then"]})
		for _, g := range m.G["elifs"] {
			s.Arms = append(s.Arms, CondArm{Cond: g.E["cond"], Body: g.B["body"]})
		}
		if g := m.G["else"]; len(g) > 0 {
			s.HasElse = true
			s.Else = g[0].B["body"]
		}
		return s
	case CSwitch:
		s := &Switch{Subject: m.E["subject"], Line: m.Line}
		for _, g := range m.G["cases"] {
			var cs Case
			for _, v := range g.G["values"] {
				cs.Values = append(cs.Values, v.E["v"])
			}
			cs.Body = g.B["body"]
			s.Cases = append(s.Cases, cs)
		}
		if g := m.G["default"]; len(g) > 0 {
			s.HasDefault = true
			s.Default = g[0].B["body"]
		}
		return s
	case CDispatch:
		s := &Dispatch{Subject: m.E["subject"], Line: m.Line}
		for _, g := range m.G["entries"] {
			s.Entries = append(s.Entries, DispatchEntry{Value: g.E["v"], Label: g.I["label"]})
		}
		if g := m.G["else"]; len(g) > 0 {
			s.Else = g[0].I["label"]
		}
		return s
	case CWhile:
		return &While{Cond: m.E["cond"], Body: m.B["body"], Line: m.Line}
	case CDoWhile:
		return &DoWhile{Body: m.B["body"], Cond: m.E["cond"], Line: m.Line}
	case CRepeatUntil:
		return &RepeatUntil{Body: m.B["body"], Cond: m.E["cond"], Line: m.Line}
	case CCFor:
		return &CFor{Init: m.S["init"], Cond: m.E["cond"], Post: m.S["post"], Body: m.B["body"], Line: m.Line}
	case CCountFor:
		s := &CountFor{Var: m.I["var"], From: m.E["from"], To: m.E["to"], Body: m.B["body"], Line: m.Line}
		if g := m.G["step"]; len(g) > 0 {
			s.Step = g[0].E["step"]
		}
		return s
	}
	panic("buildStmt: unknown construct " + string(c))
}

// ExtractFunc is the inverse of buildFunc.
func ExtractFunc(f *FuncDecl) *Match {
	m := NewMatch(f.Line)
	m.I["name"] = f.Name
	for _, p := range f.Params {
		g := NewMatch(0)
		g.I["p"] = p
		m.G["params"] = append(m.G["params"], g)
	}
	m.B["body"] = f.Body
	return m
}

// Extract is the inverse of buildStmt.
func Extract(s Stmt) (Construct, *Match) {
	m := NewMatch(0)
	switch s := s.(type) {
	case *Let:
		m.I["name"], m.E["value"] = s.Name, s.Value
		return CLet, m
	case *Assign:
		m.I["name"], m.E["value"] = s.Name, s.Value
		return CAssign, m
	case *IndexAssign:
		m.I["name"], m.E["index"], m.E["value"] = s.Name, s.Index, s.Value
		return CIndexAssign, m
	case *CallStmt:
		m.I["fn"] = s.Call.Name
		for _, a := range s.Call.Args {
			g := NewMatch(0)
			g.E["a"] = a
			m.G["args"] = append(m.G["args"], g)
		}
		return CCallStmt, m
	case *Print:
		m.E["value"] = s.Value
		if s.Newline {
			return CPrint, m
		}
		return CWrite, m
	case *Return:
		if s.Value != nil {
			g := NewMatch(0)
			g.E["value"] = s.Value
			m.G["value"] = []*Match{g}
		}
		return CReturn, m
	case *Break:
		return CBreak, m
	case *Continue:
		return CContinue, m
	case *Label:
		m.I["label"] = s.Name
		return CLabel, m
	case *Goto:
		m.I["label"] = s.Label
		return CGoto, m
	case *JumpIf:
		m.E["cond"], m.I["label"] = s.Cond, s.Label
		return CJumpIf, m
	case *If:
		m.E["cond"], m.B["then"] = s.Arms[0].Cond, s.Arms[0].Body
		for _, a := range s.Arms[1:] {
			g := NewMatch(0)
			g.E["cond"], g.B["body"] = a.Cond, a.Body
			m.G["elifs"] = append(m.G["elifs"], g)
		}
		if s.HasElse {
			g := NewMatch(0)
			g.B["body"] = s.Else
			m.G["else"] = []*Match{g}
		}
		return CIf, m
	case *Switch:
		m.E["subject"] = s.Subject
		for _, c := range s.Cases {
			g := NewMatch(0)
			for _, v := range c.Values {
				vg := NewMatch(0)
				vg.E["v"] = v
				g.G["values"] = append(g.G["values"], vg)
			}
			g.B["body"] = c.Body
			m.G["cases"] = append(m.G["cases"], g)
		}
		if s.HasDefault {
			g := NewMatch(0)
			g.B["body"] = s.Default
			m.G["default"] = []*Match{g}
		}
		return CSwitch, m
	case *Dispatch:
		m.E["subject"] = s.Subject
		for _, e := range s.Entries {
			g := NewMatch(0)
			g.E["v"], g.I["label"] = e.Value, e.Label
			m.G["entries"] = append(m.G["entries"], g)
		}
		if s.Else != "" {
			g := NewMatch(0)
			g.I["label"] = s.Else
			m.G["else"] = []*Match{g}
		}
		return CDispatch, m
	case *While:
		m.E["cond"], m.B["body"] = s.Cond, s.Body
		return CWhile, m
	case *DoWhile:
		m.E["cond"], m.B["body"] = s.Cond, s.Body
		return CDoWhile, m
	case *RepeatUntil:
		m.E["cond"], m.B["body"] = s.Cond, s.Body
		return CRepeatUntil, m
	case *CFor:
		m.S["init"], m.E["cond"], m.S["post"], m.B["body"] = s.Init, s.Cond, s.Post, s.Body
		return CCFor, m
	case *CountFor:
		m.I["var"], m.E["from"], m.E["to"], m.B["body"] = s.Var, s.From, s.To, s.Body
		if s.Step != nil {
			g := NewMatch(0)
			g.E["step"] = s.Step
			m.G["step"] = []*Match{g}
		}
		return CCountFor, m
	}
	panic("Extract: unknown statement")
}
