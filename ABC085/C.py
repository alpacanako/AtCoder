N,Y = map(int,input().split())
Y = int(Y/1000)
a = b = c = 0
flag = True
for a in range(int(Y//10)+1):
  for b in range(int((Y-10*a)//5)+1):
    c = Y-10*a-5*b
    if a+b+c == N and flag:
      flag = False
      print(a,b,c)
if flag:
  print(-1,-1,-1)
