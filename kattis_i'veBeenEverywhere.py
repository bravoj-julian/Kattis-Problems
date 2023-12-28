# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:17:54 2022

@author: danger bravo
"""
#Not working as a function
# def johnny_Cash():
#    t = int(input())
#    count = 0
#    city_list = []
#    for i in range(t):
#        n = int(input())
#        for i in range(n):
#            city = input()
#            if city not in city_list:
#                count += 1
#                # print(count)
#            city_list.append(city)
#        print(count)
#        count = 0
#        return count
# print(johnny_Cash())
        
#WORKS !!!!
t = int(input())
count = 0
city_list = []
for i in range(t):
    n = int(input())
    for i in range(n):
        city = input()
        if city not in city_list:
            count += 1
            # print(count)
        city_list.append(city)
    print(count)
    count = 0
    