import re
s = input()
K = int(input())

D = []
m = []

chars = list(set(list(s)))
chars.sort()

for n in range(3):
    if chars != []:
        m.append(min(chars))
        chars = chars[1:]

m.reverse()

t = m.pop()
D.append(t)

while len(D) < K:
    p = re.compile(t + '[a-z]')
    ma = list(set(p.findall(s)))
    ma.sort()
    if ma == []:
        if D.index(t) < len(D)-1:
            t = D[D.index(t)+1]
        else:
            t = m.pop()
            D.append(t)
    else:
        D.append(ma[0])
        t = ma[0]

D.sort()
print(D[K-1])
