# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:34:00 2022

@author: danger bravo
"""

n = input()
# print(len(n))
wordL = n.lower()
# print(wordL)
newN = ""
startN = ''
for i in range(len(n)): 
    # if "a" in n[i]:
        newN += n[i]
        # print(newN)
        if 'a' in newN:
            # print(newN[i])
            # print("This is where it should start")
            startN += n[i]
print(startN)
    

    