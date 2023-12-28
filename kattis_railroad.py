# https://open.kattis.com/problems/railroad2


# junctionyellow = 4

# switchesorange = 3


x,y = input().split()
x1= int(x) * 4
# print(x1)

# y = int(input())
y1 = int(y) * 3
# print(y1)
check = x1 + y1
if check%2 == 0:
    print("possible")
else:
    print("impossible")