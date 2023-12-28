# https://open.kattis.com/problems/ostgotska

x = input().split()
x1 = len(x)
countAe = 0
for i in range(x1):
    if 'ae' in x[i]:
        countAe +=1
percent = countAe/x1

if percent >= 0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')