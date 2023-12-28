# https://open.kattis.com/problems/tornbygge

x = int(input())
y = input().split()
towerCount= 1
firstBrick = int(y[0])
for i in range(x):
    cBrick = int(y[i])
    if cBrick > firstBrick:
        towerCount +=1
    firstBrick = cBrick
print(towerCount)
    