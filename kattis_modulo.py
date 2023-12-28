#https://open.kattis.com/problems/modulo
#https://realpython.com/python-modulo-operator/
uniqueModulo = []

for i in range(10):
    x = int(input())
    # print(x)
    y = x%42
    # print(y)
    if y in uniqueModulo:
        continue
    else:
        uniqueModulo.append(y)
# print(uniqueModulo)
print(len(uniqueModulo))