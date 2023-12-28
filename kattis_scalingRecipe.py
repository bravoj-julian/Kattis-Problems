# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 17:13:42 2023

@author: danger bravo
"""
# import math
# https://open.kattis.com/problems/scalingrecipe?tab=metadata


x, y,z = map(int,input().split())
# print(x,y,z)
ratio = z/y 
# print(ratio)
for i in range(x):
    a = int(input())
    #because of division rounding, I couldnt get correct
    # answer using first way, so used other division method
    # b = a * ratio
    # # print(a, b)
    # b = math.ceil(b)
    # # print(b)
    # this works
    # b = (a * z)/y
    b = (a / y)*z
    # this does no work
    # b = (z/y) *a
  
    print(int(b))