# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 22:32:58 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/differentdistances
# absolute Values
# https://www.mathsisfun.com/numbers/absolute-value.html


z = input()
while z != "0":
    z = z.split()
    x1 = float(z[0])
    y1 = float(z[1])
    x2 = float(z[2])
    y2 = float(z[3])
    p = float(z[4])
    # x1,y1,x2,y2,p = map(float,input().split())
    # print(x1,y1,x2,y2,p)
    x = abs(x1-x2)**p
    y = abs(y1-y2)**p
    xy= (x+y)**(1/p)
    print(round(xy,10))
    z = input()
