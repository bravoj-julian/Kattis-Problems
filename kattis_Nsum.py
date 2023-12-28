# https://open.kattis.com/problems/nsum

def n_Sum():
    n = int(input())
    n2 = input().split()
    sum = 0
    for i in range(n):
        n2[i] = int(n2[i])
        sum += n2[i]
    return sum
print(n_Sum())