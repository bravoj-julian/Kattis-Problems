# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:11:42 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/reverserot

alpha = ["a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','.']
alpha2 = alpha*2
a = input()
while a != "0":
    a = a.split(" ")
    x = a[0]
    y = a[1]
    rWord = ""
    eWord = ""
    for i in range(1,len(y)+1):
        rWord += y[-i]
    # print(rWord)
    for i in range(len(y)):
        letter = rWord[i]
        z = alpha2.index(letter.lower())
        # print(z)
        eWord += alpha2[int(z)+int(x)]
    print(eWord.upper())
    a = input()