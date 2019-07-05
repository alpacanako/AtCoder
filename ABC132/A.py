S = list(input())
str = "Yes"
for char in S:
    if S.count(char) != 2:
        str = "No"
print(str)
