N,D = map(int,input().split())
X = []
for i in range(N):
    X.append(list(map(int,input().split())))

counter = 0
for i in range(N):
    for j in range(N-i-1):
        dsquare = 0
        for k in range(D):
            dsquare += (X[i][k] - X[i+j+1][k])**2
        n = 1
        while (n**2 <= dsquare):
            if (dsquare == n**2):
                counter += 1
                break
            else:
                n += 1
print(counter)
