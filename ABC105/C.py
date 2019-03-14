N = int(input())
n = 0
k = 0
even = True
if N > 0:
    while N > 0:
        if N & 1:
            if even:
                if n & 1 << k:
                    n = n + (5<<k)
                else:
                    n = n + (1<<k)
            else:
                if n & 1 << k:
                    n = n - (1<<k)
                else:
                    n = n + (3<<k)
        even = not even
        N = N >> 1
        k += 1
else:
    N = -N
    while N > 0:
        if N & 1 != 0:
            if even:
                if n & 1 << k:
                    n = n - (1<<k)
                else:
                    n = n + (3<<k)
            else:
                if n & 1 << k:
                    n = n + (5<<k)
                else:
                    n = n + (1<<k)
        even = not even
        N = N >> 1
        k += 1
print(bin(n)[2:])
