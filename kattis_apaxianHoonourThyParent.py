# https://open.kattis.com/problems/apaxianparent

y,p = input().split()
ey =''
end = y[-1]
# print(end)
# print(y[-2:])
if y[-1] == 'e':
    ey = y+'x'+p
elif end == 'a'or end =='i'or end =='o'or end =='u':
    # replace method replaces any instances of the value you are
    # looking for starting from the smallest indexs
    # ey2 = y.replace(end,'ex')
    # ey = ey2 +p
    # i am assigning everything indexed up until the last
    # value, which allows us to just add ex '+ =
    ey = (y[:-1]+'ex'+p)
elif y[-2:] == 'ex':
    ey = y+p
else:
    ey = y +"ex"+p
print(ey)