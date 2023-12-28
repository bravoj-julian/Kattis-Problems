# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:11:39 2023

@author: danger bravo
"""

# https://open.kattis.com/problems/mixedfractions
# print(27//12)


while True:
    x = input().split()
    x1 = int(x[0])
    x2 = int(x[1])
    if x1 == 0 and x2 == 0:
        # print('end this')
        break
    mix = (x1//x2)
    conversion = x1 - (mix * x2) 
    print(mix, conversion,"/" , x2)
    
    
    
    
    