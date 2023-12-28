# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:24:44 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/missingnumbers


x = int(input())
numbers = []
numberMissed = []
for i in range(1,x+1):
    y = int(input())
    numbers.append(y)
    # print(i)
z = max(numbers)
# print(z)
if len(numbers) == z:
    print('good job')
else:    
    for i in range(1,z):
        if i in numbers:
            continue
        else:
            numberMissed.append(i)
            print(i)
    # print(numberMissed)