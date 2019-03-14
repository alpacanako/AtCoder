N,K = map(int,input().split())
A = list(map(int,input().split()))
import collections
c = collections.Counter(A)
print(N - sum([pair[1] for pair in c.most_common(K)]))
