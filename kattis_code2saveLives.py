# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:20:35 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/codetosavelives

x = int(input())
for i in range(x):
    newOut = ""
    y1 = input().split()
    z1 = input().split()
    y = int("".join(y1))
    z = int("".join(z1))
    # print(y,z)
    a = y + z
    # print(a)
    a1 = str(a)
    a2 = len(a1)
    for j in range(a2):
        newOut += a1[j] + " "
    print(newOut)