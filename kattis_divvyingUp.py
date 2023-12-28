#https://open.kattis.com/problems/divvyingup


def div_By_Three():
    n = int(input())
    purse = 0
    w = input().split()
    for i in range(n):
        r = int(w[i])
        purse += r
    # print(purse)
    if purse%3 ==0:
        x = "yes"
    else:
        x = "no"
    return x
print(div_By_Three())