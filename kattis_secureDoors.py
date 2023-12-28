# https://open.kattis.com/problems/securedoors


n = int(input())
inList = []
outList = []
for i in range(n):
    action, name = input().split()
    outList.append(name)
    action.lower()
    if action == 'entry' and name not in inList:
        print('{} entered'.format(name))
        inList.append(name)
        outList.remove(name)
    elif action == 'entry' and name in inList:
        print('{} entered (ANOMALY)'.format(name))
    elif action == 'exit' and name in inList:
        print('{} exited'.format(name))
        inList.remove(name)
        outList.append(name)
    elif action == 'exit' and name in outList:
        print('{} exited (ANOMALY)'.format(name))