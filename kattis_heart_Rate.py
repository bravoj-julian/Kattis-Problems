# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:14:58 2022

@author: danger bravo
"""


# n =22

# def heart_Rate():
#     n = int(input())
#     for i in range(n):     
#         b, p = input().split()
#         b = float(b)
#         p = float(p)
#         t = 0
#         BPM = (60*b)/p
#     # print(BPM)
#         t = BPM/b
#         minBPM = format(BPM - t, ".4f")
#     # print(minBPM)
#         maxBPM = format(BPM + t, ".4f")
#     # print(maxBPM)
#         y = minBPM, format(BPM,".4f"), maxBPM
#         print(y)
# print(heart_Rate())

n = int(input())
for i in range(n):     
      b, p = input().split()
      b = float(b)
      p = float(p)
      t = 0
      BPM = (60*b)/p
  # print(BPM)
      t = BPM/b
      minBPM = format(BPM - t, ".4f")
  # print(minBPM)
      maxBPM = format(BPM + t, ".4f")
  # print(maxBPM)
      y = minBPM + " " + format(BPM,".4f")+ " " + maxBPM
      print(y)