100 100 600
200 200 200 200 1000

100 200 800 (200~)
200 400 600 800 1800 (300~)

1 200 (200*1)
2 400 (200*2)
3 800 (100*3)
4 1000 (100*3+200)
5 1800 (200*5)
6 1900 (200*5+100)
...
------------
5 25000

2 1000
4 1000
1 1000

100 1200 (600)
200 400 600 1800 (450)
300 700 (700)




D,G = map(int,input().split())
P = []
C = []
for i in range(D):
    p,c = map(int,input().split())
    P.append(p)
    C.append(c)
