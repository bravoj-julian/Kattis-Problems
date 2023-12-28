# https://open.kattis.com/submissions/10390806

a,b,c,d,e = input().split()
score = int(input())
# print(a,b,c,d,e)
if score >= int(a):
    print('A')
elif score >= int(b):
    print('B')
elif score >= int(c):
    print('C')
elif score >= int(d):
    print('D')
elif score >= int(e):
    print('E')
else:
    print('F')