N,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
k = 0; ans = 0
while A[k] <= x:
    ans += 1
    x -= A[k]
    if k+1 == N:
        A[k] = x+1
        if x > 0:
            ans -= 1
    else:
        k += 1
print(ans)
