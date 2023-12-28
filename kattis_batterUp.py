#https://open.kattis.com/problems/batterup

t = int(input())
x = input().split()
# print(x)
total = 0
denominator = 0
for i in range(t):
    if x[i] == '-1':
        continue
    else: 
        total += int(x[i])
        denominator += 1
score = total/denominator
print(score)