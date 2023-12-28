# https://open.kattis.com/problems/apaxiaaans

name = str(input()).lower()
x = len(name)
nameCompact = ""
for i in range(x):
    # if name[i] == name[-1]:
    #     nameCompact += name[i] 
    #     break
    if i == (x-1):
        nameCompact += name[i] 
        break
    if name[i] != name[i+1]:
        nameCompact += name[i]
print(nameCompact)