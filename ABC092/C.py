N = int(input())
A = [int(i) for i in input().split()]
A[N:N] = [0]
A[0:0] = [0]

yosan = 0
for i in range(N+1):
  yosan += abs(A[i+1]-A[i])
  
for i in range(N):
  print(yosan -abs(A[i+1]-A[i]) -abs(A[i+2]-A[i+1]) +abs(A[i+2]-A[i]))
