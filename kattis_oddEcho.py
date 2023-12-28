# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:25:19 2022

@author: danger bravo
"""

o = int(input())
def oddEcho(o):
    newEcho = ""
    for i in range(o):
        n = input()
        if i %2 == 0:
            newEcho += n + "\n"
            # print(n[i])
    return newEcho
    # return e
print(oddEcho(o))

