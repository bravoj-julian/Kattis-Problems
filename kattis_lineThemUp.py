# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:04:18 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/lineup

listOG = []

x = int(input())
for i in range(x):
    y = input().upper()
    listOG.append(y)
listA = sorted(listOG)
listD = sorted(listOG, reverse= True)

if listA == listOG:
    print('INCREASING')
elif listD == listOG:
    print('DECREASING')
else:
    print('NEITHER')

# print(listA)
# print(listD)