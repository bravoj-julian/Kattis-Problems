# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 22:43:11 2022

@author: danger bravo
"""
# https://open.kattis.com/users/julian-b/submissions/avion

def ciaAvion():
    cia = ""
    count = 0
    for i in range(5):
        n = input()
        x = n.upper()
        if "FBI" in x:
            cia += str((i+1)) + " "
            count += 1
    if count == 0:
        cia = "HE GOT AWAY!"
    return cia
print(ciaAvion())

# n = input()
# x = "FBI" in n
# print(x)
# def ciaAvion():
#     cia = []
#     # cia = ""
#     count = 0
#     # ciaBlimp = 0
#     for i in range(5):
#         n = input()
#         x = n.upper()
#         if "FBI" in x:
#             cia.append(int(i+1))
#             count += 1
#     if count == 0:
#         cia = "HE GOT AWAY!"
#     return cia
# print(ciaAvion())
