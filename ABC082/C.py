import collections
N = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
ans = 0
for i in c:
    if c[i] < i:
        ans += c[i]
    elif c[i] > i:
        ans += c[i] - i
print(ans)
