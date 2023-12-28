#https://open.kattis.com/problems/digitswap

n = int(input())
reverseNumber = ""
a = str(n)
for i in range(len(a)):
    reverseNumber += a[-1-i]
    # print(reverseNumber)
print(reverseNumber)