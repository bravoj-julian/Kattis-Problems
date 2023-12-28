# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 20:19:46 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/hailstone2

x = int(input())
length = 1
n = x
hailSeq = [x]
# print(hailSeq)

while n != 1:
    if n %2 == 0:
        n = n/2
        hailSeq.append(n)
        length+=1
        # print(n)
    elif n%2 != 0:
        n = (n*3)+1
        hailSeq.append(n)
        length+=1
        # print(n)
print(length)