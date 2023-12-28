import numpy as np
# https://open.kattis.com/problems/heirsdilemma
# https://numpy.org/doc/stable/reference/generated/numpy.unique.html

#UNSOLVED 

x = input().split()
x1 = x[0] 
x2 = x[1]
uniqueCheck = []
l = int(x[0])
m = int(x[1])
y = len(x[0])
possComb = 0
checkPass = 0
divWorks = 0

for i in range(l,m):
    # print(i,m)
    intI = int(i)
    strI = str(i)
    if "0" not in strI:
        checkPass +=1
        # print('CHECK ONE PASS')
    else:continue
    for j in range(y):
        # print(strI[j])
        uniqueCheck.append(strI[j])
    checkTWO = np.unique(uniqueCheck)
    oneLength = len(checkTWO)
    # print(np.unique(uniqueCheck), "the unique characters")
    # print(len(np.unique(uniqueCheck)), "Length of unique characters")
    #print(checkTWO, "the unique characters")
    # print(oneLength, "Length of unique characters")
    # print(y, " Length of total characters")
    
    if oneLength ==  y:
        checkPass +=1
        # print("Check TWO Pass")
    else:
        continue
        uniqueCheck = []
    
    
    for k in range(y):
        #print(intI)
        # print(strI)
        #print(i, checkTWO[k])
        
        z = i%int(checkTWO[k])
        if z !=0:
            continue
        else: 
            divWorks +=1
        # z = intI/int(i[k])
        
        # zz = l//int(i[k])
        # zzz = l%int(i[k])
        # print(possComb)
        # print(zz)
        # print(zzz)
    uniqueCheck = []
    if divWorks == y:
        possComb +=1
# lValue = l.split()
# print(lValue)
# print(np.unique(uniqueCheck))
print(possComb)