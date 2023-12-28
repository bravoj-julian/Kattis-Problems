# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:48:01 2022

@author: danger bravo
"""

n = int(input())
reverseNumber = ""
a = str(n)
for i in range(len(a)):
    reverseNumber += a[-1-i]
    # print(reverseNumber)
print(reverseNumber)