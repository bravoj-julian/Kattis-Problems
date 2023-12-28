#https://open.kattis.com/problems/cold

n = input()
t = input().split()
# print(n)
# print(t)
def subZero(n,t):
    counter = 0
    nL = int(n)
    for i in range(nL): 
        tInt = int(t[i])
        if tInt < 0:
           counter += 1
    return counter
print(subZero(n,t))
