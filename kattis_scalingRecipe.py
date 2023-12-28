# https://open.kattis.com/problems/scalingrecipe?tab=metadata


x, y,z = map(int,input().split())
# print(x,y,z)
ratio = z/y 
# print(ratio)
for i in range(x):
    a = int(input())
    b = (a / y)*z
    print(int(b))