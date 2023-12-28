# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:13:15 2022

@author: danger bravo
"""

p = int(input())
# print(p)
# k, l = input().split()
# m, n = input().split()
# o, p = input().split()

def holidayCandle(p):
    for i in range(p):
        candles = 0
        k, l = input().split()
        lInt = int(l)
        for i in range(lInt):
            candles += (i+1)+1
        print(k, candles)

holidayCandle(p)