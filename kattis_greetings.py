# https://open.kattis.com/problems/greetings

s = input()
count = 0
for i in range(len(s)):
    if "e" in s[i]:
        count +=1
# print(count)
replyE = (count*2)*"e"
print("h"+replyE+"y")