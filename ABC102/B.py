N = int(input())
A = [int(i) for i in input().split()]

M = max(A)
m = min(A)
print(abs(M-m))
