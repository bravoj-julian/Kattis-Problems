# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 01:39:03 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/pervasiveheartmonitor

from sys import stdin

for line in stdin.readlines():
# line = input()
    x = line.split()
        # print(x)
    name = []
    bloodP = []
    avg = 0
    x1 = len(x)
    
    fullName = ""
    for i in range(x1):
            # print(x[i])
            if x[i].isalpha():
                name.append(x[i])
            else:
                bloodP.append(x[i])
                avg += float(x[i])
    z1 = len(name)
    y1 = len(bloodP)
    for k in range(z1):
            # print(name[k])
            fullName += name[k] + " "
    # print(name)
    print(f'{avg/y1} {fullName}')
