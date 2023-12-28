# https://open.kattis.com/problems/tri

x, y, z = map(int,input().split())
a = x + y
b = y + z
if a == z:
        ans = ('{}+{}={}'.format(x,y,z))
elif b == x:
        ans = ('{}={}+{}'.format(x,y,z))   
a = x - y
b = y - z
if a == z:
        ans = ('{}-{}={}'.format(x,y,z))
elif b == x:
        ans = ('{}={}-{}'.format(x,y,z))
a = x * y
b = y * z
if a == z:
        ans = ('{}*{}={}'.format(x,y,z))
elif b == x:
        ans = ('{}={}*{}'.format(x,y,z))        
try:
    a = x / y
    b = y / z
    if a == z:
        ans = ('{}/{}={}'.format(x,y,z))
    elif b == x:
        ans = ('{}={}/{}'.format(x,y,z)) 
except ZeroDivisionError:
        breakpoint
# x, y, z = map(int,input().split())

print(ans)


# def add(x,y,z):
#     a = x + y
#     b = y + z
#     if a == z:
#         return print('{}+{}={}'.format(x,y,z))
#     elif b == x:
#         return print('{}={}+{}'.format(x,y,z))   
# def sub(x,y,z):
#     a = x - y
#     b = y - z
#     if a == z:
#         return print('{}-{}={}'.format(x,y,z))
#     elif b == x:
#         return print('{}={}-{}'.format(x,y,z))
# def multi(x,y,z):
#     a = x * y
#     b = y * z
#     if a == z:
#         return print('{}*{}={}'.format(x,y,z))
#     elif b == x:
#         return print('{}={}*{}'.format(x,y,z))        
# def div(x,y,z):
#     try:
#         a = x / y
#         b = y / z
#         if a == z:
#             return print('{}/{}={}'.format(x,y,z))
#         elif b == x:
#             return print('{}={}/{}'.format(x,y,z)) 
#     except ZeroDivisionError:
#         breakpoint
# x, y, z = map(int,input().split())

# add(x,y,z)
# sub(x,y,z)
# multi(x,y,z)
# div(x,y,z)