Q = int(input())
for n in range(Q):
    li = list(map(int,input().split()))
    x,y = map(int,sorted(li))
    z = x + int((x*y)//(x+1)) - 1
    print(z)
