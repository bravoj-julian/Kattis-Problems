# https://open.kattis.com/problems/simonsays
# x = int(input())
# for i in range(x):
#     n = input()
#     if "Simon says" in n:
#         print(n[10:])
        
# https://open.kattis.com/problems/simon
t = int(input())
for i in range(t):
    n = input().lower()
    if "simon says" in n:
        print(n[11:])
    else:
        print("")