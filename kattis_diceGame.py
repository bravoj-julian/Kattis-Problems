# https://open.kattis.com/problems/dicegame

def addDice(x):
    value = 0
    for i  in range(len(x)):
        value += int(x[i])
    return value

g = input().split()
g1 = addDice(g)
    
e = input().split()
e1 = addDice(e)

# print(g1, e1)

if g1 == e1:
    print('Tie')
elif g1 > e1:
    print('Gunnar')
elif e1 > g1:
    print('Emma')