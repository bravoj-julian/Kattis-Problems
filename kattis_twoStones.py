# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:12:24 2022

@author: danger bravo
"""

n = int(input())
def twoStones(n):
    if n%2 == 1:
        return "Alice"
    else:
        return "Bob"
print(twoStones(n))