# https://open.kattis.com/problems/nodup

x = str(input()).upper()
# print(x)
x1 = x.split()
# print(x)
xx = len(x1)
for i in range(xx):
    n = x1[i]
    # print(n)
    if n in x1[i+1:]:
        # print("yes")
        repeated = "no"
        break
    else:
        # print("no")
        repeated = "yes"
    # for i in range(xx):
    #     if n == x1[i]:
    #         repeated = "yes"
    #         break
    #     else:
    #         repeated = "no"
print(repeated)