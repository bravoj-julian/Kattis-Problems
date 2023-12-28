# https://open.kattis.com/problems/moscowdream


a,b,c,n = map(int,input().split())
sum = a+b+c
if a>0 and b>0 and c>0 and n >=3 and sum>=n:
    print('YES')
else:
    print("NO")
# print(a,b,c,n)
