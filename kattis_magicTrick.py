# https://open.kattis.com/problems/magictrick
out = 1
s = input().lower()
for letter in s:
    r = str(s.split())
    x = r.count(letter)
    # print(x)
    if x > 1:
        out=0
        break
    if x > 1 and len(s) <=2:
        out = 1
    if len(s) <=2:
        out=0
    if len(s) <=1:
        out = 1
print(out)

# All these codes failed

# s = input().lower()
# counter = {}
# for letter in s:
#     if letter not in counter:
#         counter[letter] = 0
#     counter[letter] += 1
#     if counter[letter] > 1:
#         out = 0
#     else:
#         out = 1
        
# print(counter)

# def magicTrick():
#     out = 0
#     s = input().lower()
#     counter = {}
#     for letter in s:
#         if letter not in counter:
#             counter[letter] = 0
#         counter[letter] += 1
#     if counter[letter] > 1:
#             out = 0
#     else:
#             out = 1   
#     return out
# print(magicTrick())
# s.sort()
# for letter in s:
#     count += 1
    
# out = 0
# s = input().lower()
# counter = {}
# for letter in s:
#         if letter not in counter:
#             counter[letter] = 0
#         counter[letter] += 1
# if counter[letter] > 1:
#     out = 0
# # elif len(counter) <=2:
# #     out = 1
# else:
#     out = 1
# print(out)