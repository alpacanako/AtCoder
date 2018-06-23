N_raw = input()
N = int(N_raw)
Sn = sum([int(i) for i in list(N_raw)])

if N % Sn == 0:
    print('Yes')
else:
    print('No')

