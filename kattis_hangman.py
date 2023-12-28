# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:49:26 2022

@author: danger bravo
"""
# https://open.kattis.com/problems/hangman

n = input().upper()
guess = input().upper()
bodyParts = 10
letterCorrect = 0
letters = len(n)
for i in range(len(guess)):
    # print(n)
    # print(guess[i])
    # print(letters)
    z = guess[i]
    # print(z, "this is the letter to check for")
    x = n.count(z)
    # print(x, " the number of letters matched")
    if z not in n:
        bodyParts -= 1
        # print("wrong!", bodyParts, " chances Remaining")
    elif z in n:
        letterCorrect += x
        # i+=x
        # print("correct", i, "letters matched")
    if bodyParts == 0 and letters != letterCorrect:
        print("LOSE")
        break
    if letters == letterCorrect and bodyParts != 0:
        print('WIN')
        break
    # if letter in guess == 1:
        
    # print(bodyParts)