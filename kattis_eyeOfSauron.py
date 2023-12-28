# https://open.kattis.com/problems/eyeofsauron

inp = str(input())
def sauron(inp): 
    if "()" in inp:
        x = inp.replace("()"," ")
        # print(x)
        x = inp.split("()")
        # print(x)
    # print(x)
    # if len(x)%2 != 0:
    #     ans = "fix"
    # else:
    #     ans = "correct"
    if len(x[0]) != len(x[1]):
        ans = "fix"
    else:
        ans = "correct"
    return ans

# print(inp)
print(sauron(inp))


# x = "hello world"
# print(x)
# y = x.replace('hello', 'down')
# print(y)
