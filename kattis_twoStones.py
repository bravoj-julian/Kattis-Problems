# https://open.kattis.com/problems/twostones

n = int(input())
def twoStones(n):
    if n%2 == 1:
        return "Alice"
    else:
        return "Bob"
print(twoStones(n))