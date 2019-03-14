N,M = map(int,input().split())
S = [list(input()) for n in range(N)]
C = 0
up = down = right = left = 0
for n in range(N):
    for m in range(M):
        if S[n][m] == '.':

            d = n + 1
            while d < N:
                if S[d][m] == '.':
                    d += 1
                else:
                    down = d - n - 1
                    d = N+1
            if d == N:
                down = 

            u = n - 1
            while u >= 0:
                if S[u][m] == '.':
                    u -= 1
                else:
                    up = n - u - 1
                    u = -1

            r = m + 1
            while r < M:
                if S[n][r] == '.':
                    r += 1
                else:
                    right = r - m - 1
                    r = M

            l = m - 1
            while l >= 0:
                if S[n][l] == '.':
                    l -= 1
                else:
                    left = m - l - 1
                    l = -1

        print(down,up,right,left)
        C += (down + up) * (right + left)
        down = up = right = left = 0

print(C)

