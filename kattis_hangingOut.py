# https://open.kattis.com/problems/hangingout

l,x = input().split()
l = int(l)
x = int(x)
pTerrace = 0
rejected = 0
for i in range(x):
    entry = input().split()
    status = entry[0].lower()
    p = int(entry[1])
    
    checkAdd = pTerrace + p
    
    checkLeave = pTerrace - p
    if status == 'enter' and checkAdd <= l :
        pTerrace += p
    elif status == "enter" and checkAdd > l:
        rejected += 1
    elif status == 'leave':
        pTerrace -= p
print(rejected)
    