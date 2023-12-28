# https://open.kattis.com/problems/mult

divNumber = 0
n = int(input())
for i in range(n):
    x = int(input())
    if divNumber == 0:
        divNumber = x
        continue
    # if i == 0:
    #     divNumber = x
    #     continue
    if x%divNumber == 0:
        print(x)
        divNumber = 0
    
    # print(x)