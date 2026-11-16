import sys

def main():
    out = []
    for line in sys.stdin:
        line = line.rstrip("\n").rstrip("\r")
        chars = []
        for c in line:
            o = ord(c)
            if 48 <= o <= 57 or 65 <= o <= 90 or 97 <= o <= 122:
                if 65 <= o <= 90:
                    o += 32
                chars.append(chr(o))
        s = "".join(chars)
        if s == s[::-1]:
            out.append("yes")
        else:
            out.append("no")
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
