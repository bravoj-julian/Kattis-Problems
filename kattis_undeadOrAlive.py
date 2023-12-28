# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 18:13:01 2023

@author: danger bravo
"""
#https://open.kattis.com/problems/undeadoralive

x = input()
if ":)" in x and ":(" not in x:
   print('alive')
elif ":)" not in x and ":(" in x:
    print("undead")
elif ":)" in x and ":(" in x:
    print('double agent')
else:
    print('machine')