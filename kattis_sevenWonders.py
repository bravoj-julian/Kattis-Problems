# https://open.kattis.com/problems/sevenwonders

n = input()
z = n.upper()

def sevenWonders(n):
    z = n.upper()
    countT = 0
    countC = 0
    countG = 0
    swString = ""
    bonusPoints = 0
    for i in range(len(z)):
        # print(z[i])
        swString += z[i]
        if "T" == z[i]:
            countT += 1
            
        elif "C" == z[i]:
            countC += 1
            
        elif "G" == z[i]:
            countG += 1
    x = min(countT,countG,countC)
    # print(x)
        # if countT == countC == countG and countT !=0:  
            # bonusPoints += 7
    bonusPoints = 7*x
    basepoint = (countT**2) + (countC**2) + (countG**2)        

    totalPoints = basepoint + bonusPoints
    # print(totalPoints)
    return totalPoints
print(sevenWonders(n))