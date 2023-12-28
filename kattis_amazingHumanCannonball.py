# https://www.youtube.com/watch?v=7IwRvEoG2G0
# https://open.kattis.com/problems/humancannonball2

import math

g = 9.81

n = int(input())
for i in range(n):
    # print('hello there')
    v, a, x, h1, h2 = input().split()
    v = float(v)
    a = float(a)
    x = float(x)
    h1 = float(h1)
    h2 = float(h2)
    # print(v,a,x,h1,h2)
    
    t = x / v / math.cos(math.radians(a))
    # print(t)
    
    y = v * t * math.sin(math.radians(a)) - .5*g*t*t
    # print(y)
    # xt = v*x*(math.degrees(math.cos(a)))
    # print(xt)
    
    # yt = v*x*(math.degrees(math.sin(a)))-(1/2)*g*(x)**2
    # print(yt)
    
    if (y >= h1+1) and (y <= h2-1):
        print("Safe")
    else:
        print('Not Safe')
    
    

# # distance to wall
# x
# # height of lower wall
# h1
# # bottom of higher wall
# h2
# # velocity of cannonball
# v
# # angle of cannon
# a
# # time to reach goal
# t
# # gravity acceleration

# math.cos(x)
# Return the cosine of x radians.
# math.sin(x)
# Return the sine of x radians.

# math.degrees(x)
# Convert angle x from radians to degrees.
# math.radians(x)
# Convert angle x from degrees to radians.