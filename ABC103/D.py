N,M = map(int,input().split())
li = [[int(i) for i in input().split()] for j in range(M)]
li.sort()
a = b = C = 0
for d in li:
    if a < d[0]:
      if b <= d[0]:
        C += 1
        a = d[0]
        b = d[1]
      else:
        b = min(b,d[1])
print(C)
