N,H = map(int,input().split())
Ma = 1
B = []
for i in range(N):
    a,b = map(int,input().split())
    B.append(b)
    if a > Ma:
        Ma = a
C = 0
while H > 0:
    if B == []:
        C += int(-(-H//Ma))
        H = 0
    else:
        Mb = max(B)
        if Ma >= Mb:
            C += int(-(-H//Ma))
            H = 0
        else:
            C += 1
            H -= Mb
            B.remove(Mb)
print(C)
