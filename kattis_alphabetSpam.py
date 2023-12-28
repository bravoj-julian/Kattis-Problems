# https://open.kattis.com/problems/alphabetspam

x = str(input())
x1 = len(x)
# print(2/27)
ws = 0
lc = 0
uc = 0
symbols = 0
for i in range(x1):
    if x[i] == "_":
        ws += 1
    elif x[i].islower() == True:
        lc += 1
    elif x[i].isupper() == True:
        uc += 1
    else:
        symbols += 1
    wsScore = ws/x1
    lcScore = lc/x1
    ucScore = uc/x1
    symScore = symbols/x1
print(wsScore)
print(lcScore)
print(ucScore)
print(symScore)

