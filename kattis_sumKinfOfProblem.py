# https://open.kattis.com/problems/sumkindofproblem


p = int(input())
s1 = 0
s2 = 0
s3 = 0
count = 0
for i in range(p):
    entry = input().split()
    k = int(entry[0])
    n = int(entry[1])
    for i in range(n+1):
        s1 += i  
    
    for i in range(0,s1+1):
        if i%2 ==0:
            continue
        else:
            s2 += i
        if i ==(n*2)-1:
            break
    # for i in range(1,s1,2):
    #     s2 += i
    #     if i ==(n*2)-1:
    #         break
    
    s3 = s2+n
    # for i in range(0,s1,2):
    #     s3 += i
    #     if i ==  n*2:
    #         break
        
        
        
    print(k,s1,s2,s3)
    s1 = 0
    s2 = 0
    s3 = 0