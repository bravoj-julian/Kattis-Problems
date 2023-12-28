# https://open.kattis.com/problems/stopwatch

n = int(input())

def stopWatch(n):
    time = 0
    count = 0
    for i in range(n):
        t = int(input())
        count += 1
        # print(count, t)
        if count%2 == 0:
            time += t
            # print(count, t)
            # count += 1
        else:
            time -= t
            # print(count, t)
            # count += 1
        # print(t)
    if n%2 == 1:
        return"still running"
    else:
        return time
print(stopWatch(n))