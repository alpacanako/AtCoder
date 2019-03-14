N,M = map(int,input().split())
A = list(map(int,input().split()))
li = [[1,2],[7,3],[4,4],[5,5],[3,5],[2,5],[9,6],[6,6],[8,7]]
use = []
Q = [0]*10
counter = 0
for i in li:
    Flag = False
    if i[0] in A:
        Flag = True
        for j in use:
            if j[1] == i[1]:
                Flag = False
    if Flag:
        use.append(i)
Q[use[0][0]] = (int(N//use[0][1]))
R = N%use[0][1]
while R != 0:
    if Q[use[counter][0]] == 0 or counter+1 > len(use)-1:
        counter -= 1
    else:
        Q[use[counter][0]] -= 1
        R += use[counter][1]
        counter += 1
        Q[use[counter][0]] = int(R//use[counter][1])
        R = R%use[counter][1]
ans = ''
for i in [9,8,7,6,5,4,3,2,1]:
    ans = ans + str(i)*Q[i]
print(ans)
