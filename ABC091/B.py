N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

x = 0
a = 0

for str in s:
    x = s.count(str) - t.count(str)
    if x > a:
        a = x

print(a)
