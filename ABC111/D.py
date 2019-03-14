N = int(input())
P = []
m = -1
flag = True
for i in range(N):
    X,Y = map(int,input().split())
    P.append([X,Y])
    if m == -1:
        m = abs(X) + abs(Y)
    else:
        if (m + abs(X) + abs(Y)) % 2 == 1:
            flag = False
        if m < abs(X) + abs(Y):
            m = abs(X) + abs(Y)
if flag:
    print(m)
    print('1'+' 1'*(m-1))
    for i in range(N):
        X = P[i][0]
        Y = P[i][1]
        if X >= 0 and Y >= 0:
            xd = 'R'; yd = 'U'
        elif X < 0 and Y >= 0:
            xd = 'L'; yd = 'U'
        elif X >= 0 and Y < 0:
            xd = 'R'; yd = 'D'
        else:
            xd = 'L'; yd = 'D'
        print(xd*abs(X) + yd*abs(Y) + 'RL'*int((m-abs(X)-abs(Y))/2))
else:
    print(-1)
