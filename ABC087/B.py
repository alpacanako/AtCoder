A = int(input())
B = int(input())
C = int(input())
X = int(input())

N = 0
a = b = c = 0

for c in range(C+1):
    if (X-50*c)%100 == 0:
        for b in range(B+1):
            if (X-50*c-100*b)%500 == 0:
                if 0<= int((X-50*c-100*b)/500) <= A:
                    N += 1

print(N)
