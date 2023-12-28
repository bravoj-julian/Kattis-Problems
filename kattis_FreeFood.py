# https://open.kattis.com/problems/freefood


n = int(input())
freeFood= []
for i in range(n):
    s, t = input().split()
    s = int(s)
    t = int(t)
    for i in range(s, t+1):
        if i in freeFood:
            continue
        # print(i)
        freeFood.append(i)

print(len(freeFood))
# print(freeFood)