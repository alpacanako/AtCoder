a,b = map(str,input().split())
c = int(a+b)
flag = False
for n in range(400):
    if n*n == c:
        flag = True
if flag:
    print('Yes')
else:
    print('No')
