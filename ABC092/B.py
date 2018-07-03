N = int(input())
D,X = map(int,input().split())
A = [int(input()) for i in range(N)]
C = 0
for n in range(N):
    C += 1 + (D-1)//A[n]
print(int(C+X))
