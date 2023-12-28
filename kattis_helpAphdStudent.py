# https://open.kattis.com/problems/helpaphd

for i in range(int(input())):
    n = input()
    if '=' in n:
        print('skipped')
    else:
        n = n.split('+')
        n1 = int(n[0]) + int(n[1])
        print(n1)