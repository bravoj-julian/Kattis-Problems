# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:17:35 2022

@author: danger bravo
"""

a,b = input().split()
def greaterCheck(a, b):
    if a > b:
        return 1
    else:
        return 0
print(greaterCheck(a,b))