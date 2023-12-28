# https://open.kattis.com/problems/soylent


t = int(input())
soylent = 400
b = 0
for i in range(t):
    n = int(input())
    check = n % soylent
    if check > 0:
        b = n // soylent
        b = b+1
    else:
        b = n//soylent
    # print(check)
    print(b)