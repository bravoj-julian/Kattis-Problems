# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:09:37 2022

@author: danger bravo
"""

n = int(input())
def pot(n):
    a = 0
    for i in range(n):
        p = input()
        # for i in range(n):
        x = int(p[:-1])
        y = int(p[-1])
        z = x**y
        a += z
        # print( a)
        # p = p[:-1]**p[-1]
        # print(x)
    return a
print(pot(n))