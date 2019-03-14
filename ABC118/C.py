import math
N = int(input())
A = list(map(int,input().split()))
n = A.pop()
for i in range(N-1):
    n = math.gcd(n,A.pop())
print(n)
