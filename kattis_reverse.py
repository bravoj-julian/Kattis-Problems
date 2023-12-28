# https://open.kattis.com/problems/ofugsnuid

n = int(input())
intList = []
for i in range(n):
    x = int(input())
    intList.insert(0,x)
# intList.sort()
# print(intList)
for i in range(len(intList)):
    print(intList[i])
    
    