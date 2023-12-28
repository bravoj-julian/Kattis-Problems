# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 14:17:16 2022

@author: danger bravo
"""

n = int(input())
count = 0
schoolList = []
winners = ""
for i in range(n):
    i = input().split()
    if i[0] in schoolList:
        continue
    if count < 12:
        schoolList.append(i[0])
        winners += i[0]+" " + i[1] +"\n"
        count += 1
print(winners)
# https://open.kattis.com/problems/icpcawards 

# n = int(input())
# count = 0
# schoolList = []
# winners = []
# for i in range(n):
#     i = input().split
#     if i[0] in schoolList:
#         continue
#     if count < 12:
#         schoolList.append(i[0])
#         winners.append[i]
#         count += 1
# print(schoolList, winners)
# for i in range(12):
    # newString = str(winners[i])
    # print(winners[i])