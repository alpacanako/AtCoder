N = input()
fN = sum([int(i) for i in list(N)])
N = int(N)
if N%fN == 0:
    print('Yes')
else:
    print('No')
