N = int(input())
A = [int(a) for a in input().split(' ')]

counter = 0

l = 0
r = 0
flag = True
check_list = [0 for j in range(20)]

while r < N:

    if flag:
        A_test = A[r]

        for k in range(20):

            if A_test % (2 ** (k+1))  != 0:
                check_list[k] = check_list[k] + 1
                A_test = A_test - (2 ** k)

            if check_list[k] > 1:
                flag = False

        if flag:
            counter = counter + (r - l + 1)

    else:
        ## moving l

        A_test = A[l-1]
        flag = True

        for k in range(20):

            if A_test % (2 ** (k+1))  != 0:
                check_list[k] = check_list[k] - 1
                A_test = A_test - (2 ** k)

            if check_list[k] > 1:
                flag = False

        if flag:
            counter = counter + (r - l + 1)

    if flag:
        r = r + 1
    else:
        l = l + 1

print(counter)
