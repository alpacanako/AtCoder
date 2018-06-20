a,b = map(int,input().split())

n = b - a - 1
h = 0

for i in range(n+1):
    h = h + i

print(h-a)
