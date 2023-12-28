# -*- coding: utf-8 -*-

# https://open.kattis.com/users/julian-b/submissions/avion

def ciaAvion():
    cia = ""
    count = 0
    for i in range(5):
        n = input()
        x = n.upper()
        if "FBI" in x:
            cia += str((i+1)) + " "
            count += 1
    if count == 0:
        cia = "HE GOT AWAY!"
    return cia
print(ciaAvion())

