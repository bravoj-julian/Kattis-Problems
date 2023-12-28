# https://open.kattis.com/problems/electricaloutlets

t = "test"
outlet = 0
out = []
n = int(input())
for i in range(n):
    # k = int(input())
    k = input().split()
    for i in range(len(k)):
        out.append(k[i])
    # print(out)
    for i in range(len(k)):
        if i == 0:
            continue
        outlet += int(k[i])
    used_Out = int(k[0]) - 1
    solution = outlet - used_Out
    print(outlet)
    print(solution)
    outlet = 0
    #     o = input().split()
    #     for i in range(k):
    #         outlet += o
    #         print(outlet)

        