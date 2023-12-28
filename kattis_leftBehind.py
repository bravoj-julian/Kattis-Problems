# https://stackoverflow.com/questions/47340314/while-loop-with-two-variables-using-the-or-section-in-python
# https://open.kattis.com/problems/leftbeehind

entry = input().split()    
x = int(entry[0])
y = int(entry[1])

while not (x == 0 and y == 0):

    if x+y == 13:
        print('Never speak again.')
    elif x == y:
        print('Undecided.')
    elif x> y:
        print("To the convention.")
    elif x < y:
        print('Left beehind.')
    
    entry = input().split()
    x = int(entry[0])
    # sour jars
    y = int(entry[1])