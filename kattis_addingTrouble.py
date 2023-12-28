# -*- coding: utf-8 -*-

# https://open.kattis.com/problems/addingtrouble

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
ab = a +b
if ab ==c:
    print('correct!')
else:
    print('wrong!')