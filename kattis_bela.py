# https://open.kattis.com/problems/bela
# valueD = ['A',11],['K',4],['Q',3],['J',20],['T',10],['9',14],['8',0],['7',0]
# valueND = ['A',11],['K',4],['Q',3],['J',2],['T',10],['9',0],['8',0],['7',0]

valueD = {'A':11,'K':4,'Q':3,'J':20,'T':10,'9':14,'8':0,'7':0}
valueND = {'A':11,'K':4,'Q':3,'J':2,'T':10,'9':0,'8':0,'7':0}

# print(valueD[0][1])
# print(valueND[2][1])

n,b = input().split()
n = int(n)
b = b.upper()
points = 0
for i in range(n*4):
    x = input()
    x1 = x[0]
    # print(x1)
    x2 = x[1]
    # print(x2)
    if x2 == b:
        points += valueD[x1]
    else:
        points += valueND[x1]
print(points)
        