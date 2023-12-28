# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:54:38 2022

@author: danger bravo
"""

# volume_Level = 7
# n = int(input())
# for i in range(n):
#     n = input()
#     if n == "Skru op!" and volume_Level == 10:
#         continue
#     if n == "Skru op!":
#         volume_Level +=1
#     if n == "Skru ned!" and volume_Level == 0:
#         continue
#     if n == "Skru ned!":
#         volume_Level -=1
# print(volume_Level)


n = int(input())
def volume_Control(n):
    volume_Level = 7
    for i in range(n):
        n = input()
        if n == "Skru op!" and volume_Level == 10:
            continue
        if n == "Skru op!":
            volume_Level +=1
        if n == "Skru ned!" and volume_Level == 0:
            continue
        if n == "Skru ned!":
            volume_Level -=1
    return volume_Level
print(volume_Control(n))
