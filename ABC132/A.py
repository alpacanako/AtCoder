S = list(input())
str = "No"
if S[0] == S[1]:
    if S[2] == S[3]:
        str = "Yes"
else:
    if S.count(S[0]) == 2 and S.count(S[1]) == 2:
        str = "Yes"
print(str)
