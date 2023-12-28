# https://open.kattis.com/problems/freefood


n = int(input())
freeFood= []
for i in range(n):
    s, t = input().split()
    s = int(s)
    t = int(t)
    # https://www.w3schools.com/python/ref_func_range.asp
    for i in range(s, t+1):
        if i in freeFood:
            continue
        # print(i)
        freeFood.append(i)

print(len(freeFood))
# print(freeFood)