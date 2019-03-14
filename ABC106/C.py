S = [int(x) for x in list(input())]
K = int(input())
flag = True; i = 0
while flag:
    if S[i] == 1:
        if K == 1:
            print(1)
            flag = False
        else:
            i += 1
            K -= 1
    else:
        print(S[i])
        flag = False
