# https://open.kattis.com/problems/romans
# https://www.geeksforgeeks.org/how-to-round-numbers-in-python/

enMiles = float(input())
x = enMiles * 5280

romanMiles = 1000*(x/4854)


# print(enMiles)
print(round(romanMiles))