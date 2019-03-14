N,M = map(int,input().split())
Fav = [list(map(int,input().split()))[1:] for i in range(N)]
Sum = 0
for i in range(M):
    Flag = True
    for j in range(N):
        if not i+1 in Fav[j]:
            Flag = False
    if Flag:
        Sum += 1
print(Sum)
