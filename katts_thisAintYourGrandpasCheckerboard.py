# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:18:49 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/thisaintyourgrandpascheckerboard

board = []
rowS = []
columnS = []
moreThree = []
col = []
x = int(input())
for i in range(x):
    y = input().upper()
    board.append(y)
    # print(y)
    if y.count('W') == y.count('B'):
        rowS.append(1)
    elif y.count('W') != y.count('B'):
        rowS.append(0)
    if "WWW" in y or "BBB" in y:
        moreThree.append(0)
    else:
        moreThree.append(1)
for i in range(x):
    word =""
    for j in range(x):
        # print(board[j][i])
        word+= board[j][i]
        if j == x-1:
            if word.count('W') == word.count('B'):
                columnS.append(1)
            elif word.count('W') != word.count('B'):
                columnS.append(0)
            if "WWW" in y or "BBB" in word:
                moreThree.append(0)
            else:
                moreThree.append(1)
            col.append(word)
if 0 in rowS or 0 in columnS or 0 in moreThree:
    print(0)
else:
    print(1)
    
# checkrow
# print(board)
# print(rowS,columnS, moreThree, col)