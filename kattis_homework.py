# https://open.kattis.com/problems/heimavinna


n = input()
t1 = 0
if ";" in n:
    n1 = n.split(";")
    # print(n1)
    for i in range(len(n1)):
        if "-" in n1[i]:
            # print(n1[i])
            n2 = n1[i].split('-')
            t2 = int(n2[1]) - int(n2[0]) + 1
            # print(n2[1], n2[0])
            # print(t1)
            t1 += t2
        else:
            # print(n1[i])
            t1 += 1
            # print(t1)
            

elif "-" in n:
    n1 = n.split('-')
    t1 = int(n1[1]) - int(n1[0]) + 1
    # print(n1[1], n1[0])
    # print(t1)
    
else:
    t1 += 1
    # print(t1)
print(t1)
