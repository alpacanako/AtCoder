import math

A,B,C,D = map(int,input().split())

gcd = math.gcd(C,D)
lcm = int(C*D/gcd)

r = A%C
div_c = int((B-A+1+ +C-r)//C)
if r == 0:
    div_c += 1

r = A%D
if r == 0:
    r = -D
div_d = int((B-A+1+ +D-r)//D)

r = A%lcm
if r == 0:
    r = -lcm
div_cd = int((B-A+1+ +lcm-r)//lcm)

print(div_c, div_d, div_cd)
print(B-A+1 -div_c -div_d +div_cd)
