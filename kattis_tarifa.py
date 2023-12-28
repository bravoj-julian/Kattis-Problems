#https://open.kattis.com/problems/tarifa

x = int(input())
# print(x)
def tarifa(x):
    monthX = 0
    plus1 = 0
    n = input()
    z = int(n)
    for i in range(z):
        monthX += x
    # print(monthX)
    for i in range(z):
        p = int(input())
        # r = n[-1-i]
        plus1 += p
    y = monthX - plus1 + x
    return y
print(tarifa(x))