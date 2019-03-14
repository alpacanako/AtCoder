t = list(map(int,input()))
p = ['+','+','+']
q = ['','','']
for i in range(8):
    if i & 1:
        c = t[0] + t[1]
        p[0] = '+'
    else:
        c = t[0] - t[1]
        p[0] = '-'
    if i & (1<<1):
        c += t[2]
        p[1] = '+'
    else:
        c -= t[2]
        p[1] = '-'
    if i & (1<<2):
        c += t[3]
        p[2] = '+'
    else:
        c -= t[3]
        p[2] = '-'
    if c == 7:
        q[0] = p[0]
        q[1] = p[1]
        q[2] = p[2]
print(str(t[0]) + q[0] + str(t[1]) + q[1] + str(t[2]) + q[2] + str(t[3]) + '=7')
