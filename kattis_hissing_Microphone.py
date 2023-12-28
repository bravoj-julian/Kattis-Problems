# https://open.kattis.com/problems/hissingmicrophone

def hissing_Mic():
    n = input()
    if "ss" in n:
        x = "hiss"
    else:
        x = "no hiss"
    return x
print(hissing_Mic())