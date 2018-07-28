A,B = map(int,input().split())
S = input()
flag = True

for i in range(A):
  if not '0' <= S[i] <= '9':
    flag = False

if S[A] != '-':
  flag = False

for i in range(B):
  if not '0' <= S[A+i+1] <= '9':
    flag = False

if flag:
  print('Yes')
else:
  print('No')
