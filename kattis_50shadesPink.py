# -*- coding: utf-8 -*-
# https://open.kattis.com/problems/fiftyshades


def shade_Pink():
    n = int(input())
    count = 0
    for i in range(n):
        word=input().lower()
        if "pink" in word or "rose" in word:
            count +=1
    x = count
    if count == 0:
        x = "I must watch Star Wars with my daughter"
    return x
print(shade_Pink())


