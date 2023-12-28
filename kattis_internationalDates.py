# https://open.kattis.com/problems/internationaldates

x = input().split("/")
# print(x)
country = ""
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
if x1 <= 12 and x2 <= 12:
    country = 'either'
elif x1 > 12:
    country = "EU"
elif x2 > 12:
    country = "US"
print(country)
    