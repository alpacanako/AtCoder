N,D_1,D_2 = map(int,input().split())

P = [[i,j] for i in range(2*N) for j in range(2*N)]
B=[]

for k in range(N**2):
    B = []
    o = P[0]
    P.remove(o)
    print(o[0], o[1])
    for p in P:
        if (p[0]-o[0])**2 + (p[1]-o[1])**2 == D_1:
            B.append(p)
        if (p[0]-o[0])**2 + (p[1]-o[1])**2 == D_2:
            B.append(p)
    for b in B:
        P.remove(b)
