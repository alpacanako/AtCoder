N = int(input())
A = list(map(int,input().split()))
M = [0 for i in range(N)]

M[0] = 0
for j in range(N-1):
    M[j+1] = (A[j] - int(M[j]//2)) * 2

n = int((A[N-1] - M[0]//2 - M[N-1]//2)//2)

for i in range(N):
    if i%2 == 0:
        print(M[i] + 2*n, end=" ")
    else:
        print(M[i] - 2*n, end=" ")
