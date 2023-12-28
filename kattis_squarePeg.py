# https://open.kattis.com/problems/squarepeg

import math

l, r = map(int,input().split())
c = r * 2


# https://www.omnicalculator.com/math/square-diagonal
s = math.sqrt(2) * l
# print(c)
# print(s)
if s < c:
    print('fits')
else:
    print('nope')