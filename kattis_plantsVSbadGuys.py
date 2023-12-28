# https://open.kattis.com/problems/pvbg


x = int(input())
y = input().split()
turret = []
for i in range(x):
    turret.append(int(y[i]))
# print(turret)
# print(min(turret))
wave = min(turret)+1
print(wave)