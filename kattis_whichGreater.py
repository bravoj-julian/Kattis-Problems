# https://open.kattis.com/problems/whichisgreater

a,b = input().split()
def greaterCheck(a, b):
    if a > b:
        return 1
    else:
        return 0
print(greaterCheck(a,b))