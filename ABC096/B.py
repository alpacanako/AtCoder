A,B,C = map(int,input().split())
K = int(input())

if A >= B and A >= C:
    print(A*(2**K) + B + C)
elif B >=C:
    print(A + B*(2**K) + C)
else:
    print(A + B + C*(2**K))
