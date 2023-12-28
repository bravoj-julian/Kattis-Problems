# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 17:28:28 2022

@author: danger bravo
"""

n = input()
g, t, n = n.split()
n = int(n)
t = int(t)
g = int(g)
n2 = map(int, input().split())
x = sum(n2)
tc = (g - t)*.9
trailer = tc - x
print(int(trailer))
