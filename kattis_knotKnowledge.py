# https://open.kattis.com/problems/knotknowledge

n = int(input())
x = input().split()
y = input().split()
x1 = 0
# print(x[0])
# print(y[0])
for i in range(n):
    if (x[i]) in y:
          x1 = 0
          # print(x1)
          # print(x[i])
    else:
          x1 = int(x[i])
          # print(x1)
          break

         
print(x1)