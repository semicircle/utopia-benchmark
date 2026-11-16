import sys, re
num_re = re.compile(r'-?[0-9]+')

def evaluate(line):
    toks = line.split()
    if not toks:
        return None
    st = []
    for t in toks:
        if num_re.fullmatch(t):
            st.append(int(t))
        elif t in ('+', '-', '*', '/', '%'):
            if len(st) < 2:
                return None
            b = st.pop()
            a = st.pop()
            if t == '+':
                st.append(a + b)
            elif t == '-':
                st.append(a - b)
            elif t == '*':
                st.append(a * b)
            else:
                if b == 0:
                    return None
                q = abs(a) // abs(b)
                if (a < 0) != (b < 0):
                    q = -q
                if t == '/':
                    st.append(q)
                else:
                    st.append(a - b * q)
        else:
            return None
    if len(st) != 1:
        return None
    return st[0]

data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
out = []
for line in lines:
    r = evaluate(line)
    out.append("error" if r is None else str(r))
if out:
    sys.stdout.write("\n".join(out) + "\n")
