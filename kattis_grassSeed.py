# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:48:41 2022

@author: danger bravo
"""

def seedingGrass():
    cost = float(input())
    lawns = int(input())
    area = 0
    for i in range(lawns):
        w, l = input().split()
        w = float(w)
        l = float(l)
        area += (w*l)
        
    totalCost = area * cost
    return totalCost
print(seedingGrass())