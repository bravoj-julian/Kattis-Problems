# https://open.kattis.com/problems/addtwonumbers

a, b = input().split()
def add(a,b):
    a = int(a)
    b = int(b)
    c = a+b
    return c
print(add(a, b))