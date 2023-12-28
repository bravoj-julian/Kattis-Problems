# https://open.kattis.com/problems/cups


n = int(input())
cups = []
for i in range(n):
    entry = input().split()
    # print(entry)
    if entry[1].isdigit():
        # print("Integer")
        cups.append([entry[0], int(entry[1])])
    # print(cups)
    if entry[0].isdigit():
        holdColor = entry[1]
        holdValue = int(entry[0])/2
        # print(holdColor, holdValue)
        cups.append([holdColor, int(holdValue)])
# print(cups)

# https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/
# in order for key to work in needs a function/method to
# define what the characteristic is, So I want the
# elements in position of our list [1]
def get_radius(i):
    return i[1]

cups.sort(key=get_radius)
#key=[1])
# print(cups)
for i in range(n):
    print(cups[i][0])
    # print(cups[i]) 
   