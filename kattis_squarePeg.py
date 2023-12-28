# https://open.kattis.com/problems/squarepeg

import math

l, r = map(int,input().split())
c = r * 2
s = math.sqrt(2) * l
if s < c:
    print('fits')
else:
    print('nope')