# https://open.kattis.com/problems/trik

# a = 1
# b = 2
# c = 3
pos = 1
# print(pos)
x = input().upper()
x.split()
# print(x[0],x[1])
for i in range(len(x)):    
    if pos == 1 and x[i] == "A":
        pos = 2
    # print(pos)
    elif pos == 2 and x[i] == "A":
        pos = 1
    # print(pos)
    elif pos == 1 and x[i] == "C":
        pos = 3
    # print(pos)
    elif pos == 3 and x[i] == "C":
        pos = 1
    # print(pos)
    elif pos == 2 and x[i] == "B":
        pos = 3
    # print(pos)
    elif pos == 3 and x[i] == "B":
        pos = 2
    # print(pos)
    else:
        continue
print(pos)








#KEEP IT SIMPLE


# borko = input().upper()
# print(borko)
# bork = len(borko)
# print(bork)
# posBorko = 1
# for i in range(bork):
#     while borko[i] != "A":
#         continue
#     if borko[i] == 'A':
#         posBorko = b
#     else:
#         continue
#     if borko[i] == "B":
#         posBorko = c
#     else:
#         continue
# print(posBorko)

# if borko[i] == borko[0]:
    
# if borko[i] == 'A' and borko[i-1] == 'A':
    