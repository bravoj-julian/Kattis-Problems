# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:53:26 2022

@author: danger bravo
# """

# mon, day = input().split()
# if mon == "OCT" and day == "31":
#     print("yup")
# elif mon == "DEC" and day == "25":
#     print("yup")
# else:
#     print("nope")
    
def halloween():
    mon, day = input().split()
    if mon == "OCT" and day == "31":
        x = "yup"
    elif mon == "DEC" and day == "25":
        x = "yup"
    else:
        x = "nope"
    return x
print(halloween())