# https://open.kattis.com/problems/chopin
# when there is an unkown number of test cases 
# and there is no means to break the looop of work
# use stdin.readlines()
from sys import stdin

unique =['A', 'B', 'C', 'D', 'E', 'F','G']
notUnique = [['Bb', 'A#'],['C#','Db'],['D#','Eb'],['F#','Gb'],['G#','Ab']]
case = 0
# x = input().split()

for line in stdin.readlines():
# while True:
    x = line.split()
    if x[0] == "1":
        break
    # x = input().split()
    # print(x[0])
    case += 1
    y = x[0]
    if y in unique:
        print(f'Case {case}: UNIQUE')
    else:
       for i in range(len(notUnique)):
            # print(notUnique[i]) 
            if y in notUnique[i]:
                a = i
                b = notUnique[i].index(y)
                # print(b)
                if b == 1:
                        print(f'Case {case}: {notUnique[a][0]} {x[1]}')
                elif b == 0:
                        print(f'Case {case}: {notUnique[a][1]} {x[1]}')
                break
    # x = input().split()
