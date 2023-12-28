# https://open.kattis.com/problems/tripletexting


s = input()
x = len(s)
x1 = int(x/3)
word = []
for i  in range(0,x,x1):
    # print(i,x1)
    # print(s[i:i+x1])
    word.append(s[i:i+x1])
for i in range(len(word)):
    x2 = word.count(word[i])
    # print(x2)
    if x2 > 1:
        print(word[i])
        break