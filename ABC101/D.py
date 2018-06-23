K = int(input())

for n in range(K):
    i = int(n // 9)
    r = n % 9

    print((r+2)*(10**i) - 1)
