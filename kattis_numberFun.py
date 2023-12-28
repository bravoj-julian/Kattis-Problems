# https://open.kattis.com/problems/numberfun

def add(a,b,c):
    if a + b == c or b + a == c:
        # x = "Possible"
    # elif 
        return  "Possible"
     
def sub(a,b,c):
    if a - b == c or b - a == c:
        return  "Possible"
    #     y = "Possible"
    # elif b - a == c:
    #     y = "Possible"
    # return y
def mxx(a,b,c):
    if a * b == c or b * a == c:
        return  "Possible"
    #     x = "Possible"
    # if :
    #     x = "Possible"
    # return x
def div(a,b,c):
    if a / b == c or b / a == c:
        return  "Possible"

    #     x = "Possible"
    # if b / a == c:
    #     x = "Possible"
    # return x

n = int(input())

for i in range(n):
    entry = input().split()
    a = int(entry[0])
    b = int(entry[1])
    c = int(entry[2])
    addCheck = add(a,b,c)
    # print(addCheck)
    subCheck = sub(a,b,c)
    mxxCheck = mxx(a,b,c)
    divCheck = div(a,b,c)
    if addCheck == "Possible" or subCheck == "Possible" or mxxCheck == "Possible" or divCheck == "Possible":
        print("Possible")
    else:
        print("Impossible")
        
# print(add(1,2,3))


        