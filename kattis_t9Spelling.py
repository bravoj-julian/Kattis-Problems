# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:38:11 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/t9spelling

phoneConvert = {
    ' ' : "0",
    'a' : '2',
    'b' : '22',
    'c' : '222',
    'd' : '3',
    'e' : '33',
    'f' : '333',
    'g' : '4',
    'h' : '44',
    'i' : '444',
    'j' : '5',
    'k' : '55',
    'l' : '555',
    'm' : '6',
    'n' : '66',
    'o' : '666',
    'p' : '7',
    'q' : '77',
    'r' : '777',
    's' : '7777',
    't' : '8',
    'u' : '88',
    'v' : '888',
    'w' : '9',
    'x' : '99',
    'y' : '999',
    'z' : '9999'
    }

case = 1
x = int(input())
for i in range(x):
    y = input()
    word = ""
    for j in range(len(y)):
        z = y[j]
        a = phoneConvert[z]
        # if word == "":
        #     continue
        if j>0:
            if a[-1] == word[-1]:
                word+= " "
        word += a
    print(f'Case #{case}: {word}')
    case+=1