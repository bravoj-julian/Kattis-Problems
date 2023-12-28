# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:12:14 2022

@author: danger bravo
"""

n = input()
def autori(n):
    acronym = n[0]
    for i in range(len(n)):    
        if n[i] == "-":
            acronym +=n[i+1]
        # print("hello")
        # print(acronym)
    return acronym
print(autori(n))
