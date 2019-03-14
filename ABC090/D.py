N,K = map(int,input().split())
ans = 0
for k in range(N):
    b = k + 1
    p = int(N//b)
    r = N%b
    ans += p*max(0,b-K) + max(0,r-K+1)
if K == 0:
    ans -= N
print(ans)
