N,H = map(int,input().split())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
C = 0
while H > 0:
    Ma = max(A)
    if B == []:
        C += int(-(-H//Ma))
        H = 0
    else:
        Mb = max(B)
        if Ma > Mb:
            C += int(-(-H//Ma))
            H = 0
        else:
            C += 1
            H -= Mb
            B.remove(Mb)
print(C)
