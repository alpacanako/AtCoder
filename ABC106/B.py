N = int(input())
ans = 0
for n in range(int(-(-N//2))):
    dev = 1
    for i in range(n):
        if (2*n+1)%(2*i+1) == 0:
            dev += 1
    if dev == 8:
        ans += 1
print(ans)
