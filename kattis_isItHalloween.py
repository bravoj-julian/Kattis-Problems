# https://open.kattis.com/problems/isithalloween
    
def halloween():
    mon, day = input().split()
    if mon == "OCT" and day == "31":
        x = "yup"
    elif mon == "DEC" and day == "25":
        x = "yup"
    else:
        x = "nope"
    return x
print(halloween())