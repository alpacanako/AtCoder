N,M,X = map(int,input().split())
li = list(map(int,input().split()))
A=0
B=0
for i in range(M):
    if li.pop(0) < X:
        A=A+1
    else:
        B=B+1

print(min(A,B))
