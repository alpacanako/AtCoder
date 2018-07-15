N = int(input())
S = [input()[0] for i in range(N)]
M = S.count('M')
A = S.count('A')
R = S.count('R')
C = S.count('C')
H = S.count('H')
print(M*A*R + M*A*C + M*A*H + M*R*C + M*R*H + M*C*H + A*R*C + A*R*H + A*C*H + R*C*H)
