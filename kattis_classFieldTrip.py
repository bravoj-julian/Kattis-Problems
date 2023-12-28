# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:57:01 2023

@author: danger bravo
"""
#https://open.kattis.com/problems/classfieldtrip

ann = input()
ben = input()
x =ann + ben
# makes a list
y = sorted(x)
# unpacks all digits but seperate
y = "".join(y)
print(y)
