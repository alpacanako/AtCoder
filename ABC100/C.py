N = int(input())
li = list(map(int,input().split()))

x = 0

for n in range(N):
    a = li.pop()
    while a%2 == 0:
        x = x+1
        a = int(a/2)

print(x)
