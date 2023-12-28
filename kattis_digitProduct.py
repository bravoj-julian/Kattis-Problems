# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:39:14 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/sifferprodukt

x = input()
y = len(x)
num2multi = []
# z = len(num2multi)
for i in range(y):
    if x[i] == "0":
        # print('found 0')
        continue
    else:
        num2multi.append(x[i])
z = len(num2multi)
print(z)
while z > 1:
    
    for i in range(1,z):
        a1 = int(num2multi[i])
        a2 = int(num2multi[i-1])
        a = a1 * a2
        newA = str(a)
        
        print(a)

print(x[i])
print(num2multi)