N,K = map(int,input().split())
if K == 1:
    print(N**3)
elif K%2 == 0:
    print(int(N//K)**3 + int((N+K/2)//K)**3)
else:
    print(int(N//K)**3)
