# https://open.kattis.com/problems/judgingmoose


l,r = input().split()
l=int(l)
r=int(r)
a = ""
if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    a += 'Even '
    a += str(l*2)
else:
    a += "Odd "
if l > r:
    x = l *2
    a += str(x)
elif r > l:
    x = r*2
    a += str(x)
print(a)
 