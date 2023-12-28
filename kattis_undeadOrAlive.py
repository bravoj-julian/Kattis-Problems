#https://open.kattis.com/problems/undeadoralive

x = input()
if ":)" in x and ":(" not in x:
   print('alive')
elif ":)" not in x and ":(" in x:
    print("undead")
elif ":)" in x and ":(" in x:
    print('double agent')
else:
    print('machine')