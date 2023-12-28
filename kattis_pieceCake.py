# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:41:03 2022

@author: danger bravo
"""
# https://open.kattis.com/problems/pieceofcake2

# n, h, v = input().split()
# n = int(n) #length of the side of square
# h = int(h) # horizontal distance from cut
# v = int(v) # vertical distance from cut
# nh = n - h
# nv = n - v 
# volume = (4 * nh * nv, 4 * h * v, 4 * h * nv, 4 * nh * v)
# x = sorted(volume, reverse = True)
# # volume = 4 * nh * nv
# # volume1 = 4 * h * v
# # volume2 = 4 * h * nv
# # volume3 = 4 * nh * v
# print (x[0])

def pieceCake():
    n, h, v = input().split()
    n = int(n) #length of the side of square
    h = int(h) # horizontal distance from cut
    v = int(v) # vertical distance from cut
    nh = n - h
    nv = n - v 
    volume = (4 * nh * nv, 4 * h * v, 4 * h * nv, 4 * nh * v)
    x = sorted(volume, reverse = True)
    return x[0]
print(pieceCake())