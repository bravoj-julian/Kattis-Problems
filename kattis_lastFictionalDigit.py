# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 22:04:10 2023

@author: danger bravo
"""

# https://open.kattis.com/problems/lastfactorialdigit

x = int(input())
factor = 1

for i in range(x):
    y = int(input())
    for j in range(1,y+1):
        factor = (j*factor)
    print(str(factor)[-1])
    factor = 1