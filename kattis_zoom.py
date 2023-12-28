# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 00:33:51 2023

@author: danger bravo
"""

# https://open.kattis.com/problems/zoom

x1, x2 = map(int, input().split())
zoom = []
# zoom = ""
y = input().split()
for i in range(x2-1,x1,x2):
    zoom.append(int(y[i]))
#   zoom += y[i]+ " "
# print(zoom)
    # zoom+=y[i]
print(*zoom)