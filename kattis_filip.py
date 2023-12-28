#

n = input()
a, b = n.split()
a = str(a)
b = str(b)
z = (len(a))
# print(a, b)


def flip(a,b):
    newA = ""
    newB = ""
    for i in range(z):
        # print(a)
        newA += a[-1-i]
        # print(newA)
    for i in range(z):
        # print(a)
        newB += b[-1-i]
        # print(newB)
    reverseA = int(newA)
    reverseB = int(newB)
    if reverseA > reverseB:
        return reverseA
    else:
        return reverseB
    # return reverseA, reverseB

# reverseA = int(newA)
# reverseB = int(newB)
# largeValue = 0    
print(flip(a,b))