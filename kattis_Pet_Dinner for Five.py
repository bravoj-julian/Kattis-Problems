# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:15:18 2022

@author: danger bravo
"""

def dinner_Five():
    high_score = 0
    high_scorer = 0
    temp_score = 0
    counter = 0
    for i in range(5):   
        n = input().split()
        for i in range(4):
            temp_score += int(n[i])  
        # print(temp_score)
        counter += 1
        if temp_score > high_score:
            high_score = temp_score
            high_scorer = counter
        temp_score = 0
        # counter += 1
        # print(high_scorer)
        # print(temp_score)
        # print(counter)
    winner = (str(high_scorer) + " " + str(high_score))
    return winner
        
print(dinner_Five())
# 