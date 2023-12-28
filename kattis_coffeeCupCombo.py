# https://open.kattis.com/problems/coffeecupcombo



cTrack = 0
notSleep = 0
n = int(input())
s = input()
for i in range(n):
    s1 = int(s[i])
    if s1 == 1 and cTrack == 2:
        notSleep += 1
    # elif s1 == 1 and cTrack == 0:
    #     cTrack += 2
    #     notSleep += 1
    elif s1 == 1 and cTrack < 2:
        if cTrack == 1:
            cTrack += 1
        elif cTrack == 0:
            cTrack += 2
        notSleep += 1
    elif s1 == 0 and cTrack > 0:
        notSleep += 1
        cTrack -= 1
    else:
        continue
    # print(s[i])
print(notSleep)
    