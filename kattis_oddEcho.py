# https://open.kattis.com/problems/oddecho

o = int(input())
def oddEcho(o):
    newEcho = ""
    for i in range(o):
        n = input()
        if i %2 == 0:
            newEcho += n + "\n"
            # print(n[i])
    return newEcho
    # return e
print(oddEcho(o))

