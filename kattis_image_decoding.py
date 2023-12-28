# https://open.kattis.com/problems/imagedecoding

#UNSOLVED

n = int(input())
line = ""
length_Pixels = 0
oldPixels = 0
x = ""
while n != 0:
    for i in range(n):
        l = input().split()
        length = len(l)
        for i in range(length-1):
                r = int(l[i+1])
                length_Pixels += r
        if l[0] == "#":
            r1 ="#"
            r2 = "."
        if l[0] == ".":
            r1 ="."
            r2 = "#"
        for i in range(length):
            if l[i] == l[0]:
                continue
            r = int(l[i])
            oldPixels += r
            if i%2 == 0:
                line += (r*r2)
            if i%2 == 1:
                line += (r*r1)
        line += "\n"
        x = line
        if oldPixels%length_Pixels != 0:
            x = line + ("Error decoding image")
        length_Pixels = 0
        # x2 = ''
    # x = line
    print(x)
    n = int(input())
    oldPixels = 0
    # line = ""
    





# n = int(input())
# line = ""
# length_Pixels = 0
# oldPixels = 0
# x = ""
# while n != 0:
#     for i in range(n):
#         l = input().split()
#         length = len(l)
#         for i in range(length-1):
#             # if l[i] == l[0]:
#             #     continue    
#                 r = int(l[i+1])
#                 length_Pixels += r
#         if l[0] == "#":
#             r1 ="#"
#             r2 = "."
#         if l[0] == ".":
#             r1 ="."
#             r2 = "#"
#         for i in range(length):
#             # print("hello")
#             if l[i] == l[0]:
#                 continue
#             # print("hello 2")
#             r = int(l[i])
#             oldPixels += r
#             if i%2 == 0:
#                 line += (r*r2)
#             if i%2 == 1:
#                 line += (r*r1)
#         # print(line)
#         line += "\n"
#         # print(length_Pixels)
#         # print(oldPixels)
#         x = line

#         if oldPixels%length_Pixels != 0:
#             x = line+"Error decoding image"
#         length_Pixels = 0
#     # if oldPixels/length_Pixels ==0:
#         # print("Error decoding image")
#         # if length2 != length:
#             # print("ERROR")
#     print(x)
#     n = int(input())
#     oldPixels = 0
#     line = ""
# #print(x)
  
  