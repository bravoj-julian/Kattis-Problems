
#https://open.kattis.com/problems/classfieldtrip

ann = input()
ben = input()
x =ann + ben
# makes a list
y = sorted(x)
# unpacks all digits but seperate
y = "".join(y)
print(y)
