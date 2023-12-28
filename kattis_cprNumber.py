# https://open.kattis.com/problems/cprnummer
CPRnum = (input())
# print(CPRnum)

calNum = CPRnum.replace("-","")
# print(calNum)
sum = 0
for i in range(1):
    cpr1 = int(calNum[0]) * 4
    sum+=cpr1
    cpr2 = int(calNum[1]) * 3
    sum+=cpr2
    cpr3 = int(calNum[2]) * 2 
    sum+=cpr3
    cpr4 = int(calNum[3]) * 7
    sum+=cpr4
    cpr5 = int(calNum[4]) * 6 
    sum+=cpr5
    cpr6 = int(calNum[5]) * 5 
    sum+=cpr6
    cpr7 = int(calNum[6]) * 4 
    sum+=cpr7
    cpr8 = int(calNum[7]) * 3 
    sum+=cpr8
    cpr9 = int(calNum[8]) * 2
    sum+=cpr9
    cpr10 = int(calNum[9]) * 1
    sum+=cpr10
    if sum%11 == 0:
        ans = 1
    else:
        ans = 0
    
print(ans)