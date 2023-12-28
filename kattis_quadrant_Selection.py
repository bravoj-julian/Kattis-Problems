# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:38:13 2022

@author: danger bravo
"""

#https://open.kattis.com/problems/quadrant

x = input()
x = int(x)
y = input()
y = int(y)
if x >0 and y >0:
    quadrant = 1
if x <0 and y >0:
    quadrant = 2
if x <0 and y <0:
    quadrant = 3
if x >0 and y <0:
    quadrant = 4
print(quadrant)
