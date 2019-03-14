N,K = map(int,input().split())
x = list(map(int,input().split()))
m = abs(x[0])*2 + abs(x[N-1])*2
for i in range(N-K+1):
    if x[i] >= 0:
        t = x[i+K-1]
    elif x[i+K-1] <= 0:
        t = -x[i]
    elif -x[i] <= x[i+K-1]:
        t = -x[i]*2 + x[i+K-1]
    else:
        t = -x[i] + x[i+K-1]*2
    if t < m:
        m = t
print(m)
