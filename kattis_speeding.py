# https://open.kattis.com/problems/speeding

n = int(input())
t2 = 0
d2 = 0
speeds = []
mphx= []
for i in range(n):
    entry = input().split()
    t = int(entry[0])
    d = int(entry[1])
    speeds.append((t,d))
    # print(t,d)
    # print(speeds)
    if i == 0:
        continue
    else:
        t2 = speeds[i][0]-speeds[i-1][0]
        d2 = speeds[i][1]-speeds[i-1][1]
        mph = d2/t2
        mphx.append(mph)
        # print(mph)
mphx.sort(reverse=True)
print(int(mphx[0]))