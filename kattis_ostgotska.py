# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 02:48:53 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/ostgotska

x = input().split()
x1 = len(x)
countAe = 0
for i in range(x1):
    if 'ae' in x[i]:
        countAe +=1
percent = countAe/x1
# x = input()
# y = x.count("ae") *2
# z = x.replace(" ","")
# x1 = len(z)
# percent = y/x1
# # print((y*100)/x1)
# print(y, z, x1, percent)


# print(percent)
if percent >= 0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')