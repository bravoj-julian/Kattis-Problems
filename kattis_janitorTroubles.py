# https://open.kattis.com/problems/janitortroubles

def janitor_troubles():
    import math
    a, b, c,d = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    s = (a+b+c+d)/2 #semiperimeter
    # print(s)
    #max area equation
    k = math.sqrt((s-a)*(s-b)*(s-c)*(s-d))
    return k
print(janitor_troubles())