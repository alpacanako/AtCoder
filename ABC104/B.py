S = input()
flag = True
C = 0
l = len(S)
if not (S[0] == 'A' and 'a' <= S[1] <= 'z' and 'a' <= S[l-1] <= 'z' ):
    flag = False
i = 2
while i < l-1:
    if not 'a' <= S[i] <= 'z':
        if S[i] == 'C':
            C += 1
        else:
            flag = False
    i += 1
if flag and C == 1:
    print('AC')
else:
    print('WA')
