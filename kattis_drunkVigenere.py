# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 01:05:10 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/drunkvigenere


alpha = ["a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# print(alpha.index("z"))
# print(len(alpha))
alpha2 = alpha*2
# print(alpha2)
encrypt = input().lower()
key = input().lower()
decryptWord = ""
for i in range(len(key)):
    if i == 0 or i%2 == 0:
        encrValue = alpha2.index(encrypt[i],25)
        # print(encrypt[i], encrValue)
        keyValue = alpha.index(key[i])
        # print(key[i], keyValue)
        newLetter = encrValue - keyValue
        # print(newLetter, alpha2[newLetter], "this is the decrypted letter")
        decryptWord += alpha2[newLetter].upper()
    else:
        encrValue = alpha2.index(encrypt[i])
        # print(encrypt[i], encrValue)
        keyValue = alpha.index(key[i])
        # print(key[i], keyValue)
        newLetter = encrValue + keyValue
        # print(newLetter, alpha2[newLetter], "this is the decrypted letter")
        decryptWord += alpha2[newLetter].upper()
print(decryptWord)





# alphaDict = {
#         "A":0,
#         "B":1,
#         "C":2,
#         "D":3,
#         "E":4,
#         "F":5,
#         "G":6,
#         "H":7,
#         "I":8,
#         "J":9,
#         "K":10,
#         "L":
#     }