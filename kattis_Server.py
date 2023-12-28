# https://open.kattis.com/problems/server

n, T = map(int,input().split())
n1 = input().split()
taskT = 0
taskC = 0
for i in range(n):
    # print(n1[i])
    taskT += int(n1[i])
    if taskT <= T:
        taskC +=1
print(taskC)