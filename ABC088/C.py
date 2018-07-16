c11,c12,c13 = map(int,input().split())
c21,c22,c23 = map(int,input().split())
c31,c32,c33 = map(int,input().split())

if c12 - c11 == c22 - c21 == c32 - c31 and c13 - c12 == c23 - c22 == c33 - c32:
    print('Yes')
else:
    print('No')
