N = int(input())
A = [int(a) for a in input().split(' ')]

counter = 0

Abi = []

for a in A:
    bi = []
    A_test = a
    for k in range(20):
        if A_test % (2 ** (k+1)) != 0:
            bi.append(1)
            A_test = A_test - (2 ** k)
        else:
            bi.append(0)
    Abi.append(bi)

l = 0
r = 0
flag = True
check_list = [0 for j in range(20)]

while r < N:

    if flag:
        for k in range(20):
                check_list[k] = check_list[k] +  Abi[r][k]

        if check_list.count(2) > 0:
            flag = False

        if flag:
            counter = counter + (r - l + 1)

    else:
        flag = True

        for k in range(20):
            check_list[k] = check_list[k] - Abi[l-1][k]

        if check_list.count(2) > 0:
            flag = False

        if flag:
            counter = counter + (r - l + 1)

    if flag:
        r = r + 1
    else:
        l = l + 1

print(counter)
