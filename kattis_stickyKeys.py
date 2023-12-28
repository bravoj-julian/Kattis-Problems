# https://open.kattis.com/problems/stickykeys

s = input()
s1 = len(s)
# print(s1)
newString = ""
for i in range(0,s1):
    # print(s[i])
    # print(i)
    # print(s[i])
    if i == s1-1:
        # print("IT WILL END NEXT TURN")
        newString +=s[i]
        break
    # if s[i] == s[-1]:
        # break
    # if s[i] == s[i+1]:
    #     print("THIS WORKS - SKIP THE LETTER")
    #     continue    
    # else:
    #     newString += s[i]
        
    if s[i] != s[i+1]:
        newString += s[i]
           
    else:
         # print("THIS WORKS - SKIP THE LETTER")
        continue  
        
print(newString)