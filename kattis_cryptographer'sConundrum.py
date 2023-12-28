# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:04:36 2023

@author: danger bravo
"""

# alpha = ["a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# print(alpha.index("z"))
# print(len(alpha))

# https://open.kattis.com/problems/conundrum

day = 0
x = input().upper()
# print(x)
x1 = int(len(x))
# print(x1)
for i in range(0,x1,3):
    if x[i] != "P":
        # x[i] = "P"
        day += 1
        # print(x[i], 'p')
        i+=1
    else:
        # print("correct order", x[i])
        i+=1
    if x[i] !="E":
        # x[i] = "E"
        day+=1
        # print(x[i], 'e')
        i+=1
    else:
        # print("correct order", x[i])
        i+=1
    if x[i] !="R":
        # x[i] = "R"
        day+=1
        # print(x[i], 'r')
        i+=1
    else: 
        # print("correct order", x[i])
        i+=1
print(day)