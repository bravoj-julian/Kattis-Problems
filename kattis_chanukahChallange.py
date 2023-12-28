#https://open.kattis.com/problems/chanukah

p = int(input())

def holidayCandle(p):
    for i in range(p):
        candles = 0
        k, l = input().split()
        lInt = int(l)
        for i in range(lInt):
            candles += (i+1)+1
        print(k, candles)

holidayCandle(p)