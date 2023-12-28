# https://open.kattis.com/problems/bus

t = int(input())
sBus = 0
for i  in range(t):
    y = int(input())
    for i in range(y):
    # print(sBus)
    # step1 = sBus + .5
    # print(step1)
    # sBus = step1 * 2
        sBus = (sBus + .5)*2
    # print(sBus)
    print(int(sBus))
    sBus = 0