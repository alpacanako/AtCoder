N,M,Q = map(int,input().split())
memo = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    l,r = map(int,input().split())
    memo[l][r] += 1
for i in range(N):
    for j in range(N):
        memo[i+1][j+1] += memo[i][j+1] + memo[i+1][j] - memo[i][j]
for i in range(Q):
    p,q = map(int,input().split())
    print(memo[q][q] - memo[p-1][q] - memo[q][p-1] + memo[p-1][p-1])
