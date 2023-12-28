# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:03:23 2022

@author: danger bravo
"""

# https://open.kattis.com/problems/jobexpenses
def jobExpenses():
    n = input()
    k = input().split()
    expenses = 0
    for i in range(len(k)):
        if "-" in k[i]:
            e = int(k[i])
            expenses += e
    expenses = expenses * -1
    return expenses
print(jobExpenses())