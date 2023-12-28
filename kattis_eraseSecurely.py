
# https://open.kattis.com/problems/erase

x = int(input())
y = input()
y1 = input()
z = len(y)
yList = list(y)

for i in range(x):
    for j in range(z):
        # print(yList[j], "what it was Og")
        if yList[j] == "0":
            yList[j] = "1"
            # print(yList[j], "what it changed to")
        elif yList[j] == "1":
            yList[j] = "0"
            # print(yList[j], "what it changed to")
    # print(*yList)
sameBits = 0
# check
for i in range(z):
    if y[j] == y1[j]:
        sameBits += 1
if yList == list(y1):
    print('Deletion succeeded')
else:
    print("Deletion failed")
