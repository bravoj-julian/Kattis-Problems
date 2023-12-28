# https://open.kattis.com/problems/jackolanternjuxtaposition

n = input(" Input your value N,T,M value must be between 1 and 500: ")
n, t, m = n.split()
n = int(n)
t = int(t)
m = int(m)
out = n * t * m
print(out)