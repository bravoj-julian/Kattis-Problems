# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:04:18 2022

@author: danger bravo
"""

# scientific structures. There are three types of scientific structure
#  cards: Tablet (‘T’), Compass (‘C’), and Gear (‘G’). For each type 
#  of cards, a player earns a number of points that is equal to the 
#  squared number of that type of cards played. Additionally, for each
#  set of three different scientific cards, a player scores 7  points.

# For example, if a player plays 3 Tablet cards, 2 Compass cards and  
# 1 Gear card, she gets 21 points points.
# The input has a single string with no more than 50 characters.
#  The string contains only letters ‘T’, ‘C’ or ‘G’, which denote the 
#  scientific cards a player has played in a Seven Wonders game.

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
    # print("t" ,countT,countT**2 )
    # print("c", countC, countC**2)
    # print("g", countG, countG**2)
    # print(swString)
    # print(basepoint)   
    # print(bonusPoints)
    totalPoints = basepoint + bonusPoints
    # print(totalPoints)
    return totalPoints
print(sevenWonders(n))