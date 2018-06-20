A,B,K = map(int,input().split())

if A+K < B-K+1:
    for n in range(K):
        print(A+n)
    for n in range(K):
        print(B-K+n+1)
else:
    for n in range(B-A+1):
        print(A+n)
