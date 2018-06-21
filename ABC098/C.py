N = int(input())
S = list(input())

m = N
x = S.count('E')

for i in S:
    if i == 'E':
        x = x - 1

    if x < m:
        m = x

    if i == 'W':
        x = x + 1

print(m)
