# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 18:22:58 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/addingtrouble

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
ab = a +b
if ab ==c:
    print('correct!')
else:
    print('wrong!')