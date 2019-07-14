L,R = map(int,input().split())
ans = 2019
if (R-L+1 >= 2019):
    ans = 0
else:
    for i in range(R-L+1):
        for j in range(R-L-i):
            ans = min(ans,( ( (L+i)%2019) * ((L+i+j+1)%2019) ) % 2019 )
print(ans)
