# https://open.kattis.com/problems/jumbojavelin

def jumbo_javelin():
    n = int(input())
    javelin = 0
    for i in range(n):
        n1 = int(input())
        javelin += n1
        loss_length = 1*(n-1)
        total_length = javelin - loss_length
    return total_length
print(jumbo_javelin())