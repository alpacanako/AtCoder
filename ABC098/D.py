N = int(input())
A = [int(a) for a in input().split(' ')]

counter = 0

l = 0
r = 0
flag = True
xor = 0
sum = 0

while r < N and l < N:
    if flag:
        xor ^= A[r]
        sum += A[r]
        if xor == sum:
            counter += (r - l + 1)
        else:
            flag = False
    else:
        xor ^= A[l-1]
        sum -= A[l-1]
        if xor == sum:
            counter += r - l + 1
            flag = True

    if flag:
        r += 1
    else:
        l += 1

print(counter)
