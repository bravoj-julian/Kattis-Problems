# https://open.kattis.com/problems/licensetolaunch

def byDay(day):
    return day[1]



dayDebris=[]
n = int(input())
entry = input().split()
for i in range(n):
    dayDebris.append((int(entry[i]),int(i)))
# print(dayDebris)
dayDebris.sort()
# print(dayDebris)

print(dayDebris[0][1])


