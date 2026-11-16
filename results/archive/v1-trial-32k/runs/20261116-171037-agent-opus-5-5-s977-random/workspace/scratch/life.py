import random,sys,subprocess
random.seed(5)
for t in range(30):
    h=random.randint(1,20); w=random.randint(1,20); g=random.randint(0,30)
    G=[[random.random()<0.4 for _ in range(w)] for _ in range(h)]
    inp=f"{g}\n"+"".join("".join('#' if c else '.' for c in r)+"\n" for r in G)
    for _ in range(g):
        N=[[False]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                c=sum(G[a][b] for a in range(i-1,i+2) for b in range(j-1,j+2) if 0<=a<h and 0<=b<w and (a,b)!=(i,j))
                N[i][j]= c==3 or (c==2 and G[i][j])
        G=N
    exp="".join("".join('#' if c else '.' for c in r)+"\n" for r in G)
    out=subprocess.run(["../bin/dushpek","run","../solutions/t2-life.dus"],input=inp,capture_output=True,text=True)
    if out.stdout!=exp: print("FAIL",t,out.stderr); break
else: print("all ok")
