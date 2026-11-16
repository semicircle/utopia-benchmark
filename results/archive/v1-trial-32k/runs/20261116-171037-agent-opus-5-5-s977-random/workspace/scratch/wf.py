import random,re,subprocess,collections,time
random.seed(7)
vocab=[''.join(random.choice('abcXYZdeQ') for _ in range(random.randint(1,5))) for _ in range(300)]
for t,nl in enumerate([0,1,5,50,2000]):
    lines=[]
    for _ in range(nl):
        lines.append(''.join(random.choice(vocab)+random.choice([' ',', ','.','1','  ','-',"'"]) for _ in range(random.randint(0,15))))
    inp=''.join(l+'\n' for l in lines)
    c=collections.Counter(w.lower() for w in re.findall('[A-Za-z]+',inp))
    exp=''.join(f'{w} {n}\n' for w,n in sorted(c.items(),key=lambda x:(-x[1],x[0]))[:10])
    t0=time.time()
    out=subprocess.run(["../bin/dushpek","run","../solutions/t2-wordfreq.dus"],input=inp,capture_output=True,text=True)
    print(nl, out.stdout==exp, out.stderr, time.time()-t0, sum(c.values()))
