# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:17:21 2022

@author: danger bravo
"""
import math
def sibice():
    
    n,w,h = input().split()
    w = int(w)
    h = int(h)
    n = int(n)
    d = w**2 + h**2
    d = math.sqrt(d)
    output = ""
    # print(d)
    for i in range(n):
        n = int(input())
        if n <= d:
            output += "DA\n"
        elif n > d:
            output += "NE\n"
    return output
print(sibice())
        
    