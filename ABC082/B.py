s = list(input())
t = list(input())
s.sort()
flag = True
i = 0
ans = False
while flag:
    ans = False
    for x in t:
        if s[i] < x:
            flag = False
            ans = True
        elif s[i] == x:
            ans = True
    if ans and flag:
        t.remove(s[i])
        if i + 1 < len(s):
            i += 1
        elif t == []:
            flag = False
            ans = False
        else:
            flag = False
            ans = True
    elif not ans:
        flag = False
if ans:
    print('Yes')
else:
    print('No')
