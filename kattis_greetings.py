# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:32:10 2022

@author: danger bravo
"""

s = input()
count = 0
for i in range(len(s)):
    if "e" in s[i]:
        count +=1
# print(count)
replyE = (count*2)*"e"
print("h"+replyE+"y")