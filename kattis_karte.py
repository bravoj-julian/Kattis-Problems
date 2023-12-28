# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:01:58 2023

@author: danger bravo
"""
# https://open.kattis.com/problems/karte

s = input()
cardHave = []
s1 = len(s)
P = 13
K = 13
H = 13
T = 13
answer = P, K, H, T
for i in range(0,s1, 3):
    card = s[i:i+3]
    # print(i)
    # print(s[i:i+3])
    if card in cardHave:
        print('GRESKA')
        P = ""
        K= ""
        H=""
        T=""
        break
    
    if card not in cardHave:
        # print('not in List')
        if s[i] == 'P':
            P -= 1
        if s[i] == 'K':
            K -= 1
        if s[i] == 'H':
            H -= 1
        if s[i] == 'T':
            T -= 1
        cardHave.append(s[i:i+3])
        
    
    # print(cardHave)
    # answer 
print(P, K, H, T)