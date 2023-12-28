# https://open.kattis.com/problems/dicecup
n,m = input().split()

n1 = int(n)+1
m1 = int(m)+1
if n1 == m1:
    print(n1)
else:
    lowValue = min([n1,m1])
    highValue = max(n1,m1)
    # print(lowValue, highValue)
    for i in range(highValue+1):
        if i<lowValue:
            continue
        else:
            print(i)
    