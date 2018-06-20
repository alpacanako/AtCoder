n = int(input())
li = list(map(int,input().split()))

M = max(li)
li.remove(M)

N = int(M//2)
li_sa = [abs(li[i] - N) for i in range(n-1)]
m = min(li_sa)
k = li_sa.index(m)

N = li[k]

print(str(M)+" "+str(N))
