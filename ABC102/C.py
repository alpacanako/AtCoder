N = int(input())
A = [int(i) for i in input().split()]
B = [A[i]-i for i in range(N)]
B.sort()
b = B[int(N//2)]
C = [abs(B[i]-b) for i in range(N)]
print(sum(C))
