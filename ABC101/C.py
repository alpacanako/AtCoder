N,K = map(int,input().split(' '))
A = [int(i) for i in input().split(' ')]

if K == 2:
    print(N-1)
elif N % (K-1) > 1:
    print(N // (K-1) + 1)
else:
    print(N // (K-1))
