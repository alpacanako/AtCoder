S = input()
T = input()
flag = False
for i in range(len(S)):
    if S[i:] + S[:i] == T:
        flag = True
if flag:
    print('Yes')
else:
    print('No')
