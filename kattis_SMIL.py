# https://open.kattis.com/problems/smil

# smiles = ":)", ";)", ':-)', ';-)'
x = input()
xlen = len(x)
x1 = x.find(":)")
x2 = x.find(';)')
x3 = x.find(':-)')
x4 = x.find(';-)')
# print(x1,x2,x3,x4)
smilesLocation = []
for i in range(xlen):
    if ":)" == x[i:i+2]:
        # print("try 1")
        smilesLocation.append(i)
    elif ";)" == x[i:i+2]:
        # print("try 1")
        smilesLocation.append(i)
    elif ":-)" == x[i:i+3]:
        # print("try 1")
        smilesLocation.append(i)
    elif ";-)" == x[i:i+3]:
        # print("try 1")
        smilesLocation.append(i)
# print(smilesLocation)
for i in range(len(smilesLocation)):
    print(smilesLocation[i])