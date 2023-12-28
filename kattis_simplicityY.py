# https://open.kattis.com/problems/simplicity
#UNSOLVED

x = input().lower()
a = [word for word in x]
y = len(set(a))
#print(y)
if y == 1 or y ==2:
    z = 0
else:
    z = abs(2-y)
print(z)

#USING NUMPY
# import numpy as np
# x = input().lower()
# a = [word for word in x]
# y = len(np.unique(a))
# #print(y)
# if y == 1 or y ==2:
#     z = 0
# else:
#     z = abs(2-y)
# print(z)