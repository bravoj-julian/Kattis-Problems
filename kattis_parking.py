# https://open.kattis.com/problems/parking2

t = int(input())
dist = 0
minimalDistance = 0
dist1 = []
for i in range(t):
    n = int(input())
    x = input().split()
    for i in range(n):
        dist1.append(int(x[i]))  
    for i in range(n-1):
        x2 = sorted(dist1, reverse = True)
        # print(x2)
        dist = int(x2[i]) - int(x2[i+1])
        minimalDistance += dist
    minimalDistance = minimalDistance * 2
    print(minimalDistance)
    minimalDistance = 0
    dist = 0
    dist1 =[0]


# t = int(input())
# dist = 0
# minimalDistance = 0
# for i in range(t):
#     n = int(input())
#     x = input().split()
#     x2 = sorted(x, reverse = True)
#     print(x2)
#     for i in range(n-1):
#         print(x2)
#         dist = int(x2[i]) - int(x2[i+1])
#         minimalDistance += dist
#     minimalDistance = minimalDistance * 2
#     print(minimalDistance)
#     minimalDistance = 0
#     dist = 0
    
    
# def parkingDist():
#     t = int(input())
#     dist = 0
#     minimalDistance = 0
#     for i in range(t):
#         n = int(input())
#         x = input().split()
#         x2 = sorted(x, reverse = True)
#         for i in range(n-1):
#             # print(x2)
#             dist = int(x2[i]) - int(x2[i+1])
#             minimalDistance += dist
#         minimalDistance = minimalDistance * 2
#         return minimalDistance
# print(parkingDist())