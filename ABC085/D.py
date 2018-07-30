N,H = map(int,input().split())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
C = 0
while H > 0:
    C += 1
    Ma = max(A)
    if B == []:
        H -= Ma
    else:
        Mb = max(B)
        if Ma > Mb:
            H -= Ma
        else:
            H -= Mb
            B.remove(Mb)
print(C)
