li = list(map(int,input().split()))
X,Y,Z = map(int,sorted(li))

W = (Z-X) + (Z-Y)

if W%2 == 0:
    print(int(W//2))
else:
    print(int(W//2+2))
