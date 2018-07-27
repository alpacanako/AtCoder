N = int(input())
C = []
S = []
F = []

for i in range(N-1):
  c,s,f = map(int,input().split())
  C.append(c)
  S.append(s)
  F.append(f)

# 時刻xで駅iにいて,最短で向かった場合の駅Nへの到着時刻
def time(i,x):
  if i == N:
    return x
  else:
    # 直近の列車の出発時刻tを求める
    a = int(-(-x//F[i-1]))
    t = max(a*F[i-1],S[i-1])
    return time(i+1,t+C[i-1])

for i in range(N):
  print(time(i+1,0))
