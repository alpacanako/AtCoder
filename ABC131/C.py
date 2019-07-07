import math

A,B,C,D = map(int,input().split())

gcd = math.gcd(C,D)
lcm = int(C*D/gcd)

ans_A = int((A-1) - (A-1)//C - (A-1)//D + (A-1)//lcm)
ans_B = int(B - B//C - B//D + B//lcm)
print(ans_B - ans_A)
