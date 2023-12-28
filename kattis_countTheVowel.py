# https://open.kattis.com/problems/countthevowels

vowelCount = str(input())
# vowels = "a" or "e" or "i" or "o" or "u"
count = 0
x = len(vowelCount)
vowelCount = vowelCount.lower()
# print(x)
for i in range(x):   
    # print(i)
    if "a" == vowelCount[i]:
        # print("it works")
        count += 1
        # print(vowelCount[i])
    if "e" == vowelCount[i]:
        # print("it works")
        count += 1
        # print(vowelCount[i])
    if "i" == vowelCount[i]:
        # print("it works")
        count += 1
        # print(vowelCount[i])
    if "o" == vowelCount[i]:
        # print("it works")
        count += 1
        # print(vowelCount[i])
    if "u" == vowelCount[i]:
        # print("it works")
        count += 1
        # print(vowelCount[i])
print(count)
    

