# https://open.kattis.com/problems/nastyhacks

def nasty_Hack():
    n  = int(input())
    for i in range(n):
        r,e,c = input().split()
        r = int(r)
        e = int(e)
        c = int(c)
        if e-c > r:
            a = "advertise"
            # print(a)
            # return a
        elif e-c == r:
            a = "does not matter"
            # return b
            # print(b)
        elif e-c < r:
            a = "do not advertise"
            # print(c)
    # return a and b and c
            # print("do not advertise")
        # print(a)
    return a
print(nasty_Hack())


# this code also works
n  = int(input())
for i in range(n):
    r,e,c = input().split()
    r = int(r)
    e = int(e)
    c = int(c)
    if e-c > r:
        a = "advertise"
        print(a)
            # return a
    elif e-c == r:
        a = "does not matter"
            # return b
        print(a)
    elif e-c < r:
        a = "do not advertise"
        print(a)