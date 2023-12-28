# https://open.kattis.com/problems/detaileddifferences

times = int(input())
output = ""
for x in range(times):
    # print(string1)
    string1 = input()  
    string2 = input()
    length = len(string1)
    for x in range(length):
        if string1[x] != string2[x]:
            # print("*")
            output += "*"
        else:
            output += "."
    print(string1)
    print(string2)
    print(output)
    output=""
    
    