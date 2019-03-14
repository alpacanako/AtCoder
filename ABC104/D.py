S = input()
l = len(S)
Q = S.count('?')
ans = 0
for i in range(l-2):
    for j in range(l-i-2):
        for k in range(l-i-j-2):
            d = 3**Q
            s1 = S[i]; s2 = S[i+j+1]; s3 = S[i+j+k+2]
            if s1 == 'A' or s1 == '?':
                if s1 == '?':
                    d /= 3
                if s2 == 'B' or s2 == '?':
                    if s2 == '?':
                        d /= 3
                    if s3 == 'C' or s3 == '?':
                        if s3 == '?':
                            d /= 3
                        ans += d
                        ans = ans%(10**9+7)
print(int(ans))
