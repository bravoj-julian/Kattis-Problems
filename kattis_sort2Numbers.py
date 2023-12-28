# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 21:15:07 2022

@author: danger bravo
"""

a,b = input().split()
def sort2(a,b):
    a = int(a)
    b = int(b)
    amin = str(a) + " " + str(b)
    bmin = str(b) + " " + str(a)
    if a < b:
        return amin
    elif a == b:
        return amin
    else:
        return bmin
    
print(sort2(a,b))