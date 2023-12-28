# https://open.kattis.com/problems/symmetricorder

n = int(input())
nameListFwd = []
nameListBack = []
setN = 0
while n !=0:
    for i in range(n):
        entry = input()
        if i%2 == 0:    
            nameListFwd.append(entry)
        # print(entry+"top")
        else:
            nameListBack.insert(0, entry)
        # print(entry+"bottom4")
        fullList = nameListFwd + nameListBack
# print(fullList)
    setN += 1
    print("SET",setN)
    for i in range(len(fullList)):
        print(fullList[i])
    nameListFwd = []
    nameListBack = []
    n = int(input())