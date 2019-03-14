N = int(input())
flag = False
for n in range(int(N//4)+1):
    for m in range(int(N//7)+1):
        if (4*n) + (7*m) == N:
            flag = True
if flag:
    print('Yes')
else:
    print('No')
