# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:04:07 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/bookingaroom

import random as rm

x = input().split()
x1 = int(x[0])
x2 = int(x[1])
# print(x)
bookedRoom = []

for i in range(x2):
    y = int(input())
    bookedRoom.append(y)
# print(bookedRoom)
if x2 == x1:
    print('too late')
else:
    z = rm.randint(1,x1)
    while z in bookedRoom:
        z = rm.randint(1,x1)
    print(z)
