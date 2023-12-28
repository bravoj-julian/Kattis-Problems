# https://pythonexamples.org/python-find-index-of-item-in-list/
# https://open.kattis.com/problems/relocation

# the number of companies to track / # how many queries will be run
n,q = input().split()
n1 = int(n)
q1 = int(q)
#  the location 
x = input().split()

for i in range(q1):
    # print("test")
    # x1[1] ======== the company number
    # x1[2] ======== the new value associanted to that index
    x1 = input().split()
    if x1[0] == "1":
        cpChange = int(x1[1])-1
        x[cpChange] =x1[2]
        # cpChange = x.index(x1[1])
        # x[cpChange] = x1[2]
        # print(x)
    if x1[0] == "2":
        # print(x)
        if x1[1] == 1:
            dd = int(x[0])
        elif x1[1] == n1:
            dd = int(x[n1])
        elif x1[2] == n1:
            d2 = int(x[n1])
        elif x1[2] == 1:
            d2 = int(x[0])
        else:
        
            dx = int(x1[1])
            # print(dd)
            dd = x[dx-1]
            # print(dd)
        
            dx2 = int(x1[2])
            # print(dd)
            d2 = x[dx2-1]
            # print(d2)
        
        diff = int(dd) - int(d2)
        if diff < 0:
            diff = diff *(-1)
        print(diff)


# for i in range(q1):
#     # print("test")
#     x1 = input().split()
#     if x1[0] == "1":
#         # x[1] = x1[2]
#         cpChange = x.index(x1[1])
#         x[cpChange] = x1[2]
#         # cpChange = x1[1]
#         # if cpChange == 1:
#         #     cpChange = 0
#         # elif cpChange == n:
#         #     cpChange = n
#         # else:
#         #     x[cpChange-1] = x1[2]
#         # print(x)
#     if x1[0] == "2":
#         # print(x)
#         # # for i in range(n1):
#         # #     # while n1[i] != x1[1]:
#         # dist1 = x.index(x1[1])
#         # # print(dist1)
#         # dist2 = x.index(x1[2])
#         # # print(dist2)
#         # if dist2 == 0:
#         #     dist2 = 1
#         # if dist1 == 0:
#         #     dist1 = 1            
#         # distance = dist1 - dist2
#         # # print(type(distance))
#         # print(distance)
#             # x2 = int(x1[1])
#             # x3 = int(x1[2])
#         # the difference comes from the value of what is index[i]
#         # so 2 4 5 means the 4th indexed value minus the 5th index value 
#         if x1[1] == 1:
#             dd = int(x[0])
#         elif x1[1] == n1:
#             dd = int(x[n1])
#         elif x1[2] == n1:
#             d2 = int(x[n1])
#         elif x1[2] == 1:
#             d2 = int(x[0])
#         else:
        
#             dx = int(x1[1])
#             # print(dd)
#             dd = x[dx-1]
#             # print(dd)
        
#             dx2 = int(x1[2])
#             # print(dd)
#             d2 = x[dx2-1]
#             # print(d2)
        
#         diff = int(dd) - int(d2)
#         if diff < 0:
#             diff = diff *(-1)
#         print(diff)
#         # dx1 = int(x1[1])
#         # dist1 = x[dx1]
#         # print(dist1)
        
#         # dx2 = int(x1[2])
#         # dist2 = x[dx2]
#         # print(dist2)
        
        
        
# # print(x)

# 5 10
# 5 2 8 1 4
# 1 2 10
# 2 4 5
# 2 1 3
# 1 4 3
# 2 1 5
# 2 5 2
# 1 4 1
# 2 2 4
# 1 3 15
# 2 4 1