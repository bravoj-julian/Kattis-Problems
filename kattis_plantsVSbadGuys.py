# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:59:20 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/pvbg


x = int(input())
y = input().split()
turret = []
for i in range(x):
    turret.append(int(y[i]))
# print(turret)
# print(min(turret))
wave = min(turret)+1
print(wave)