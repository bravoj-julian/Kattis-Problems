# https://open.kattis.com/problems/magictrick
out = 1
s = input().lower()
for letter in s:
    r = str(s.split())
    x = r.count(letter)
    # print(x)
    if x > 1:
        out=0
        break
    if x > 1 and len(s) <=2:
        out = 1
    if len(s) <=2:
        out=0
    if len(s) <=1:
        out = 1
print(out)
