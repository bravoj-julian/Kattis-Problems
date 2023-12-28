# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:12:30 2022

@author: danger bravo
"""
# https://open.kattis.com/problems/oddities
n = int(input())
for i in range(n):
    x = int(input())
    if x%2 ==0:
        print(x , " is even")
    else:
        print(x , " is odd")
    # print(x)