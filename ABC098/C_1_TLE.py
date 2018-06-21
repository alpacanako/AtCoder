N = int(input())
S = list(input())

m = S.count('W')
x = 0

for i in range(N):
    x = S.count('E')
    if x < m:
        m = x

    if S[i] == 'W':
        S[i] = 'E'
    else:
        S[i] = 'W'

print(m)
