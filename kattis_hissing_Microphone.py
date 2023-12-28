# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:01:21 2022

@author: danger bravo
"""
# https://open.kattis.com/problems/hissingmicrophone
def hissing_Mic():
    n = input()
    if "ss" in n:
        x = "hiss"
    else:
        x = "no hiss"
    return x
print(hissing_Mic())