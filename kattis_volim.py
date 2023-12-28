# https://open.kattis.com/problems/volim



# boxHolder
k = int(input())

# # of questions asked to players
n = int(input())
seconds = 0
boxplode = 210

for i in range(n):
    # seconds passed and answer
    t = input().split()
    seconds += int(t[0])
    t[1] = t[1].upper()
    if boxplode <= seconds:
        # print(k)
        continue
    if t[1] == "T":
        k += 1
        if k == 9:
            k = 1
        # print(k)
    elif t[1] == "N" or t[1] =='S':
        continue
print(k)
# print(seconds)