# https://open.kattis.com/problems/cetvrta

x1,x2 = input().split()
x3,x4 = input().split()
x5,x6 = input().split()
x7 = 0
x8 = 0
for i in range(1):
    if x1 == x3:
        x7 = x5
    elif x1 == x5:
        x7 = x3
    else:
        x7 = x1
for i in range(1):
    if x2 == x4:
       x8 = x6
    elif x2 == x6:
        x8 = x4
    else:
        x8 = x2
print(x7, x8)
