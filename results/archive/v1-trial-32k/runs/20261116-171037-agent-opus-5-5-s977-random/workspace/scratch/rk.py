import random,subprocess,bisect
random.seed(3)
for t in range(20):
    xs=sorted(random.randint(-20,20) for _ in range(random.randint(0,30)))
    qs=[random.randint(-25,25) for _ in range(50)]
    inp=' '.join(map(str,xs))+'\n'+''.join(f'{q}\n' for q in qs)
    exp=''.join(f"{bisect.bisect_left(xs,q)} {'found' if q in xs else 'missing'}\n" for q in qs)
    out=subprocess.run(["../bin/dushpek","run","../solutions/t1-rank.dus"],input=inp,capture_output=True,text=True)
    if out.stdout!=exp: print("FAIL",inp,out.stderr);break
else: print("rank ok")
def rpn(line):
    toks=line.split()
    if not toks: return "error"
    st=[]
    for tk in toks:
        if tk in "+-*/%" and len(tk)==1:
            if len(st)<2: return "error"
            b=st.pop();a=st.pop()
            if tk in "/%" and b==0: return "error"
            q=abs(a)//abs(b)*(1 if (a<0)==(b<0) else -1) if b else 0
            st.append({'+':a+b,'-':a-b,'*':a*b,'/':q,'%':a-b*q}[tk])
        else:
            s=tk[1:] if tk.startswith('-') else tk
            if not s.isdigit(): return "error"
            st.append(int(tk))
    return str(st[0]) if len(st)==1 else "error"
L=[]
for _ in range(500):
    L.append(' '.join(random.choice(['+','-','*','/','%',str(random.randint(-9,9)),str(random.randint(-9,9)),str(random.randint(0,9)),'x','-0']) for _ in range(random.randint(0,7))))
inp=''.join(l+'\n' for l in L)
exp=''.join(rpn(l)+'\n' for l in L)
out=subprocess.run(["../bin/dushpek","run","../solutions/t2-rpn.dus"],input=inp,capture_output=True,text=True)
print("rpn", out.stdout==exp, out.stderr, sum(e!='error\n' for e in exp.splitlines(True)))
