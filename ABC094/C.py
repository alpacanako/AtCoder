N = int(input())
n = int(N/2)

li = list(map(int,input().split()))
li_s = sorted(li)

A = li_s[n-1]
B = li_s[n]

for i in range(N):
    if li[i] <=A:
        print(B)
    else:
        print(A)
