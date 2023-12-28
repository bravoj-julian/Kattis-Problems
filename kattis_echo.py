# https://open.kattis.com/problems/echoechoecho

n = input().strip()
echo = ""
for i in range(3):
    echo += n + " "
# a = n * 3
print(echo)