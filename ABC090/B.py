def kaibun(n):
  m = list(str(n))[::-1]
  if m == list(str(n)):
    return True
  else:
    return False

A,B = map(int,input().split())
c = 0
for d in range(B-A+1):
  if kaibun(A+d):
    c += 1
print(c)
