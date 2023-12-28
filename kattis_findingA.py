# https://open.kattis.com/problems/findingana

n = input()
# print(len(n))
wordL = n.lower()
# print(wordL)
newN = ""
startN = ''
for i in range(len(n)): 
    # if "a" in n[i]:
        newN += n[i]
        # print(newN)
        if 'a' in newN:
            # print(newN[i])
            # print("This is where it should start")
            startN += n[i]
print(startN)
    

    