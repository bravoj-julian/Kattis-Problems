# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:57:34 2022

@author: danger bravo
"""

# https://www.youtube.com/watch?v=Zrp7NyO12ho
# math.sin(math.radians()) sin function returns answer in radians,
# so, use radians function to convert to degrees.
# hheght / sin(anfgle)
# https://open.kattis.com/problems/ladder
def ladder():
    import math 
    # import numpy as nmp
    h, v = input().split()
    h = int(h)
    v = int(v)
    vv = math.sin(math.radians(v))
    length = h//vv + 1
    # using // rounds division down,so we can just add 1
    length = int(length)
    # length = int(nmp.ceil(length))
    return length
print(ladder())