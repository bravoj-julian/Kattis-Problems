# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:36:59 2022

@author: danger bravo
"""


x = int(input())
# print(x)
def tarifa(x):
    monthX = 0
    plus1 = 0
    n = input()
    z = int(n)
    for i in range(z):
        monthX += x
    # print(monthX)
    for i in range(z):
        p = int(input())
        # r = n[-1-i]
        plus1 += p
    y = monthX - plus1 + x
    return y
print(tarifa(x))