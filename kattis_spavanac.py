# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:11:28 2022

@author: danger bravo
"""

h, m = input().split()
# hour = int(h)
# minute = int(m)

# print(h, m)
def alarmClock(h,m):
    hour = int(h)
    minute = int(m)
    alarmSet = 45
    if minute < 45:
        if hour == 0:
            hour = 23
        else:
            hour = hour - 1
        minute = minute + 60 - alarmSet  
    else:
        minute = minute - alarmSet  
    # print(hour)
    # minute = minute + 60 - alarmSet  
    if minute == 60:
        minute = 0
    time = str(hour) + " " + str(minute)
    return  time

print(alarmClock(h,m))
