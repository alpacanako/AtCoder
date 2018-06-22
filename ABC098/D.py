N = int(input())
A = [int(a) for a in input().split(' ')]

counter = 0

for i in range(N):
    d = 0
    flag = True
    check_list = [0 for j in range(20)]

    while flag:
        counter = counter + 1
        A_test = A[i+d]
#        print(i,i+d)

        for k in range(20):

            if flag and A_test % (2 ** (k+1))  != 0 and check_list[k] > 0:
                counter = counter - 1
#                print("no",i,i+d)
                d = 0
                flag = False

            elif A_test % (2 ** (k+1))  != 0:
                check_list[k] = check_list[k] + 1
                A_test = A_test - (2 ** k)

#            print(check_list)

#        print(flag)

        if i + d + 1 >= N:
            flag = False
        else:
            d = d + 1

print(counter)
