# https://open.kattis.com/problems/ultimatebinarywatch

a0 = '....'
a1 ='...*'
a2 = '..*.'
a3 = '..**'
a4 = '.*..'
a5 = '.*.*'
a6 = '.**.'
a7 = '.***'
a8 = '*...'
a9 = '*..*'

n = input()

t1 = ""
t2 = ""
t3 = ""
t4 = ""


for i in range(4):
    
    def addLine():
        global t1, t2, t3, t4
        t1 += ax1
        t2 += ax2
        t3 += ax3
        t4 += ax4
    if i == 1 or i == 3:   
    # if i == 2:
        # print(" ")
        ax1 = (' ')
        ax2 = (' ')
        ax3 = (' ')
        ax4 = (' ')
        addLine()
    
    if i == 2:   
    # if i == 2:
        # print(" ")
        ax1 = ('   ')
        ax2 = ('   ')
        ax3 = ('   ')
        ax4 = ('   ')
        addLine()
        
    if n[i] == '0':
        # print(a1)
        ax1 = (a0[0])
        ax2 = (a0[1])
        ax3 = (a0[2])
        ax4 = (a0[3])
        addLine()
        
    if n[i] == '1':
        # print(a1)
        ax1 = (a1[0])
        ax2 = (a1[1])
        ax3 = (a1[2])
        ax4 = (a1[3])
        addLine()

    if n[i] == '2':
        # print(a2)
        ax1 = (a2[0])
        ax2 = (a2[1])
        ax3 = (a2[2])
        ax4 = (a2[3])
        addLine()
        
    if n[i] == '3':
        # print(a3)
        ax1 = (a3[0])
        ax2 = (a3[1])
        ax3 = (a3[2])
        ax4 = (a3[3])
        addLine()
        
    if n[i] == '4':
        # print(a4)
        ax1 = (a4[0])
        ax2 = (a4[1])
        ax3 = (a4[2])
        ax4 = (a4[3])
        addLine()
        
    if n[i] == '5':
        # print(a5)
        ax1 = (a5[0])
        ax2 = (a5[1])
        ax3 = (a5[2])
        ax4 = (a5[3])
        addLine()
        
    if n[i] == '6':
        # print(a6)
        ax1 = (a6[0])
        ax2 = (a6[1])
        ax3 = (a6[2])
        ax4 = (a6[3])
        addLine()
        
    if n[i] == '7':
        # print(a7)
        ax1 = (a7[0])
        ax2 = (a7[1])
        ax3 = (a7[2])
        ax4 = (a7[3])
        addLine()
        
    if n[i] == '8':
        # print(a8)
        ax1 = (a8[0])
        ax2 = (a8[1])
        ax3 = (a8[2])
        ax4 = (a8[3])
        addLine()
        
    if n[i] == '9':
        # print(a9)
        ax1 = (a9[0])
        ax2 = (a9[1])
        ax3 = (a9[2])
        ax4 = (a9[3])
        addLine()


print(t1)
print(t2)
print(t3)
print(t4)




# a0 = '....'
# a1 ='...*'
# a2 = '..*.'
# a3 = '..**'
# a4 = '.*..'
# a5 = '.*.*'
# a6 = '.**.'
# a7 = '.***'
# a8 = '*...'
# a9 = '*..*'

# n = input()

# t1 = []
# t2 = []
# t3 = []
# t4 = []
    
# for i in range(4):
#     def addLine():
#         t1.append(ax1)
#         t2.append(ax2)
#         t3.append(ax3)
#         t4.append(ax4)
        
#     if i == 2:
#         # print(" ")
#         ax1 = (' ')
#         ax2 = (' ')
#         ax3 = (' ')
#         ax4 = (' ')
#         addLine()
        
#     if n[i] == '0':
#         # print(a1)
#         ax1 = (a0[0])
#         ax2 = (a0[1])
#         ax3 = (a0[2])
#         ax4 = (a0[3])
#         addLine()
        
#     if n[i] == '1':
#         # print(a1)
#         ax1 = (a1[0])
#         ax2 = (a1[1])
#         ax3 = (a1[2])
#         ax4 = (a1[3])
#         addLine()

#     if n[i] == '2':
#         # print(a2)
#         ax1 = (a2[0])
#         ax2 = (a2[1])
#         ax3 = (a2[2])
#         ax4 = (a2[3])
#         addLine()
        
#     if n[i] == '3':
#         # print(a3)
#         ax1 = (a3[0])
#         ax2 = (a3[1])
#         ax3 = (a3[2])
#         ax4 = (a3[3])
#         addLine()
        
#     if n[i] == '4':
#         # print(a4)
#         ax1 = (a4[0])
#         ax2 = (a4[1])
#         ax3 = (a4[2])
#         ax4 = (a4[3])
#         addLine()
        
#     if n[i] == '5':
#         # print(a5)
#         ax1 = (a5[0])
#         ax2 = (a5[1])
#         ax3 = (a5[2])
#         ax4 = (a5[3])
#         addLine()
        
#     if n[i] == '6':
#         # print(a6)
#         ax1 = (a6[0])
#         ax2 = (a6[1])
#         ax3 = (a6[2])
#         ax4 = (a6[3])
#         addLine()
        
#     if n[i] == '7':
#         # print(a7)
#         ax1 = (a7[0])
#         ax2 = (a7[1])
#         ax3 = (a7[2])
#         ax4 = (a7[3])
#         addLine()
        
#     if n[i] == '8':
#         # print(a8)
#         ax1 = (a8[0])
#         ax2 = (a8[1])
#         ax3 = (a8[2])
#         ax4 = (a8[3])
#         addLine()
        
#     if n[i] == '9':
#         # print(a9)
#         ax1 = (a9[0])
#         ax2 = (a9[1])
#         ax3 = (a9[2])
#         ax4 = (a9[3])
#         addLine()


# print(t1)
# print(t2)
# print(t3)
# print(t4)