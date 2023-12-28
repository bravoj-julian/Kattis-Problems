# https://open.kattis.com/problems/plantingtrees
 # Jon can choose the order of planting the trees as he likes, so he wants to plant the trees in such a way that the party will be as soon as possible.


n = int(input())
t = list(map(int,input().split()))
t.sort(reverse=True)
# print(t)
t2g = []
day = 1
for i in range(n):
    s = int(t[i])
    t2g.append(day+s)
    day+=1
e = max(t2g) + 1
print(e)