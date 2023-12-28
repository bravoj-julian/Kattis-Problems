# https://open.kattis.com/problems/moderatepace

# https://byjus.com/maths/median/


def bySecond(var):
    return var[1]

n = int(input())
valueList=[]
tempList=[]
finalList=[]
for i in range(3):    
    entry = input().split()
    for j in range(len(entry)):
        valueList.append(((int(entry[j])),int(j)))
    print('')
    print('New Team')
valueList.sort(key=bySecond)
print(valueList)
for i in range(3):
    for j in range(n*3):
        print(valueList[i][0])
        tempList.append((str(valueList[i][0])))
        tempList.sort()
print(tempList)
finalList.append([tempList[1]])
print(finalList)