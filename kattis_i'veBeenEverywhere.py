# https://open.kattis.com/problems/everywhere

t = int(input())
count = 0
city_list = []
for i in range(t):
    n = int(input())
    for i in range(n):
        city = input()
        if city not in city_list:
            count += 1
            # print(count)
        city_list.append(city)
    print(count)
    count = 0
    