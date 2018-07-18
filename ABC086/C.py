t = x = y = 0
T = [0]
X = [0]
Y = [0]

N = int(input())
for i in range(N):
    t,x,y = map(int,input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

f = True
d = s = 0
for i in range(N):
    d = (T[i+1]-T[i]) - abs(X[i+1]-X[i]) - abs(Y[i+1]-Y[i])
    if f and d >= 0 and d%2 == 0:
        f = True
    else:
        f = False

if f:
    print('Yes')
else:
    print('No')
