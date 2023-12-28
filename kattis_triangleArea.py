# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:22:12 2022

@author: danger bravo
"""
# https://open.kattis.com/submissions/9545857
h, b = input().split()
def triangleArea(h,b):
    b = int(b)
    h = int(h)
    a = h * (b*(1/2))
    return a
print(triangleArea(h,b))