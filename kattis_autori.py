#https://open.kattis.com/problems/autori

n = input()
def autori(n):
    acronym = n[0]
    for i in range(len(n)):    
        if n[i] == "-":
            acronym +=n[i+1]
        # print("hello")
        # print(acronym)
    return acronym
print(autori(n))
