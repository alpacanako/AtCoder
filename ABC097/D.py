N,M = map(int,input().split())
p = list(map(int,input().split()))
S = []
for i in range(M):
    x,y = map(int,input().split())
    if x < y:
        S.append([x,y])
    elif x > y:
        S.append([y,x])
M.sort()
