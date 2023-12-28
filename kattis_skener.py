# https://open.kattis.com/problems/skener

r,c,rZ,cZ = input().split()
r = int(r)
c = int(c)
rZ = int(rZ)
cZ = int(cZ)
a = ""
ax = ''
rx = ''
count = 0

for i in range(r):
    # print("before\n",a)
    x = input()
    # print(x[0],x[1],x[2])
    # print(x)
    for i in range(c):
        ax += (x[i] * cZ)
    for i in range(rZ):    
        a+= ax+'\n'
    ax=''

   
print(a)
# print(ar)
# for i in range(r):
#     print(a)



# for i in range(r):
#     # d = ('.')
#     if i %2 == 0:
#         d = '.'
#     else:
#         d = 'x'
#     a += d
#     a += a*rZ
#     print(a)
#     count += 1
#     print(count)
#     for j  in range(c-1):
#         #     d = "."
        
#         # d1 = 'x'
#         if count%2 == 0:
#             if j %2 == 0:
#                 d = '.'
#             else:
#                 d = 'x'
#             # a += d
#             a += d *cZ
#         else:     
#             if j %2 == 0:
#                 d = 'x'
#             else:
#                 d = '.'
#             # a += d
#             a += d *cZ
#         # print(j)
#     a += '\n'
# print(a)


        # a +=ax
        
    # a +='\n'
    
    
    # ax += (x[i] * cZ)
    # print(ax)
    # a += ax
    # print(a)
    
   
    
    # print("after\n",a)
    # a += a*rZ
    # print("cZ")
    # a += x*cZ+'\n'
    # a += x+"\n"
    # for i in range(rZ-1):      
    #     a += a#+'\n'
    # print('rZ')