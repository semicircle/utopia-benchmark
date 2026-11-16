import sys

def is_int(tok):
    s = tok
    if s.startswith("-"):
        s = s[1:]
    if len(s) == 0:
        return False
    for ch in s:
        if not ("0" <= ch <= "9"):
            return False
    return True

def trunc_div(a, b):
    q = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        q = -q
    return q

def main():
    out = []
    for line in sys.stdin:
        line = line.rstrip("\n").rstrip("\r")
        tokens = line.split()
        stack = []
        err = False
        for tok in tokens:
            if is_int(tok):
                stack.append(int(tok))
            elif tok in ("+", "-", "*", "/", "%"):
                if len(stack) < 2:
                    err = True
                    break
                b = stack.pop()
                a = stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    if b == 0:
                        err = True
                        break
                    q = trunc_div(a, b)
                    if tok == "/":
                        stack.append(q)
                    else:
                        stack.append(a - b * q)
            else:
                err = True
                break
        if err or len(stack) != 1:
            out.append("error")
        else:
            out.append(str(stack[0]))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
