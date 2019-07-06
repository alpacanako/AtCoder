import math

A,B,C,D = map(int,input().split())

gcd = math.gcd(C,D)
lcm = int(C*D/gcd)

comp = int(((lcm//C) + (lcm//D) - 1) * ((B-A+1)//lcm))

for i in range((B-A+1)%lcm):
    if (A+i)%C == 0 or (A+i)%D == 0:
        comp += 1

print(B-A+1-comp)
