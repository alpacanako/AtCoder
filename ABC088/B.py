N = int(input())
A = [int(a) for a in input().split()]
A.sort()
A.reverse()
d = 0
for a in A[::2]:
  d += a
for a in A[1::2]:
  d -= a
print(d)
