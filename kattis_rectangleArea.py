# https://open.kattis.com/problems/rectanglearea


x1, y1, x2, y2 = input().split()
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)


length = x2 - x1 
width = y2 - y1
# print(length, width)
area = length*width
if area < 0:
    area = area*-1
print(round(area,3))