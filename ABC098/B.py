N = int(input())
S = input()

count = 0

for n in range(N):
    x = 0
    Sl = S[:n]
    Sr = S[n:]
    for a in set(S):
        if a in Sl and a in Sr:
            x += 1
    if count < x:
        count = x

print(count)
