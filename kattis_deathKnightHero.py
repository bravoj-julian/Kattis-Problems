# https://open.kattis.com/problems/deathknight

n = int(input())
count = 0
for i in range(n):
    k = input().upper()
    if "CD" not in k:
        count += 1
print(count)