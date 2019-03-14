N = [int(i) for i in input()]
if N[0] > N[1] or (N[0]==N[1] and N[0] >= N[2]):
    print(N[0]*111)
else:
    print((N[0]+1)*111)
