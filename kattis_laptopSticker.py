# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 13:37:26 2022

@author: danger bravo
"""
# https://open.kattis.com/problems/laptopsticker

def laptop_Sticker():
    
    wc, hc, ws, hs = input().split()
    wc = int(wc) - 2
    hc = int(hc) - 2
    ws = int(ws)
    hs = int(hs)
    if ws <= wc and hs <= hc:
        x = 1
    else:
        x = 0
    return x
print(laptop_Sticker())