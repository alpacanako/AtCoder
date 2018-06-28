def beki(n,X):
    # the maximum of the form n**k under X
    x = 1
    while x*n <= X:
        x *= n
    if x == n:
        return 1
    else:
        return(x)

X = int(input())
a = 1

for n in range(X)[2:]:
    b = beki(n,X)
    if b > a:
        a = b

print(a)
