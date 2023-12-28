# https://open.kattis.com/problems/speedlimit

x = input()
miles = 0
while x != "-1":
    # print("test")
    for i in range(int(x)):
        s,t = input().split()
        s= int(s)
        t = int(t)
        if i == 0:
            miles += s*t
            x = t
            # print(miles)
            # print(x)
        else:
            # print(x)
            # print(t)
            tx = t-x
            # print(tx)
            miles += tx*s
            x = t
            
            # print(t-x)
            # print(miles)
        # print(s)
        # print(t)
        # miles += s 
    print(miles, "miles")
    miles = 0
    x = input()
