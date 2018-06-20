D,N = map(int,input().split())

if N < 100:
    X = (100 ** D) * N
else:
    X = (100 ** D) * (N+1)

print(X)
