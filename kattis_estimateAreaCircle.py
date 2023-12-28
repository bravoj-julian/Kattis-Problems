# https://open.kattis.com/problems/estimatingtheareaofacircle

# def areaCirle():
    # while True:
    #     r, m, c = input().split()
    #     r = float(r)
    #     m = int(m)
    #     c = int(c)
    #     sqr = (r*2) **2
    #     if r == 0 and m == 0 and c == 0:
    #         break
    #     st1 = (r**2) * 3.141592654
    #     nd2 = (c / m) * sqr
    #     x = print(st1, nd2)
        
# print(areaCirle())

while True:
    r, m, c = input().split()
    r = float(r)
    m = int(m)
    c = int(c)
    sqr = (r*2) **2
    if r == 0 and m == 0 and c == 0:
        break
    st1 = (r**2) * 3.141592654
    nd2 = (c / m) * sqr
    print(st1, nd2)