# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 02:36:00 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/tornbygge

x = int(input())
y = input().split()
towerCount= 1
firstBrick = int(y[0])
for i in range(x):
    cBrick = int(y[i])
    if cBrick > firstBrick:
        towerCount +=1
    firstBrick = cBrick
print(towerCount)
    