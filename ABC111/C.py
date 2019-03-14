import collections

n = int(input())
v = list(map(int,input().split()))

vodd = [v[2*i] for i in range(int(n/2))]
veven = [v[2*i+1] for i in range(int(n/2))]

codd = collections.Counter(vodd)
ceven = collections.Counter(veven)

aodd = codd.most_common()[0][0]
aeven = ceven.most_common()[0][0]

nodd = codd.most_common()[0][1]
neven = ceven.most_common()[0][1]

if aodd != aeven:
    print(n-nodd-neven)
else:
    if len(codd) == 1:
        if len(ceven) == 1:
            print(n-nodd)
        else:
            meven = ceven.most_common()[1][1]
            print(n-nodd-meven)
    elif len(ceven) == 1:
        modd = codd.most_common()[1][1]
        print(n-modd-neven)
    else:
        modd = codd.most_common()[1][1]
        meven = ceven.most_common()[1][1]
        print(min(n-nodd-meven,n-modd-neven))
