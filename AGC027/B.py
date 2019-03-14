N,X = map(int,input().split())
x = list(map(int,input().split()))
# list of used energies
L = [0]
for i in range(1,1<<N):
    # t will be the used enerdy
    # suteru energy
    t = X
    # k will be the current amount of trashes
    k = 0
    first = True
    #j2 = 0
    for j in range(N):
        j = N - j - 1
        if i & 1<<j:
            if first:
                # go right
                t += x[j]
                first = False
            else:
                # go left
                t += (k + 1)*(k + 1)*(x[j2] - x[j])
            j2 = j
            # hirou energy
            t += X
            k += 1
    # go left to point zero
    t += (k + 1)*(k + 1)*(x[j2])
    L.append(t)

ans = -1
for j in range(1<<(N*N)):
    M = 0
    m = 0
    for l in range(N):
        k = j>>N*l & ((1<<N)-1)
        M |= k
        m += L[k]
    if M == (1<<N)-1:
        if m < ans or ans == -1:
            ans = m
print(ans)
