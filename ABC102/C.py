N = int(input())
A = [int(i) for i in input().split()]
B = [abs(A[i]-i-1) for i in range(N)]
b = int(sum(B)/N)
print(min(abs(sum(B)-b*N),abs(sum(B)-b*N-b)))
