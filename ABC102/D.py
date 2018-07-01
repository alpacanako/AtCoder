def f(A,a):
    B = []
    while sum(B) < a and A != []:
        B.append(A.pop())
    if abs(sum(B)-a) > abs(sum(B[:-1])-a) and B != []:
        A.append(B.pop())
    if B == []:
        B.append(A.pop())
    return(B)

N = int(input())
A = [int(i) for i in input().split()]
B = f(A,int(sum(A)/2 + 0.5))
C = f(A,int(sum(A)/2 + 0.5))
D = f(B,int(sum(B)/2 + 0.5))
Y = [sum(X) for X in [A,B,C,D]]
print(max(Y)-min(Y))
