# https://open.kattis.com/problems/makingameowth

# n = the page kepwth will read
# p = pages i will read
# x = minutes to read i will rake
# y = minures to read  meowth

countI = 0
countMeow = 0

n,p,x, y = input().split()
n = int(n)
p = int(p)
x = int(x)
y = int(y)
n1 = n -1
nx = n1
for i in range(p):
    # if n1 == n:
    #     countMeow +=1
    #     n1 += n
    #     # p +=1
    # else:
    #     countI += 1
    countI += 1
    # print(countI)   

    if countI == nx:
        countMeow += 1
        # print(countMeow)

        nx += n1
        # print(nx)
timeI = countI * x
timeMeow = countMeow * y
totalTime = timeI + timeMeow
# print(timeI)
# print(timeMeow)   
# print(countMeow)
# print(countI)   
print(totalTime)
    
11
2
11
2
11
2
11
2
11
2
11
2
11
2

