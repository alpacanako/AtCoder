N = int(input())
A1 = [int(i) for i in input().split()]
A2 = [int(i) for i in input().split()]

a = 0
for i in range(N):
    a = max(a,sum(A1[:i+1]) + sum(A2[i:]))
print(a)
