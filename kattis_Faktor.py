# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:31:04 2022

@author: danger bravo
"""
# import numpy

a, i = input().split()
def citationReq(a,i):
    a = int(a)
    i = int(i) - 1
    c = (a*i) +1
    # d = int(c)
    # e = a//i
    # f = int(numpy.ceil(c))
    return c

print(citationReq(a,i))


