# https://open.kattis.com/problems/taisformula
# https://github.com/DMamrenko/Kattis-Problems/blob/main/tais_formula.py

# number of glucose samples
n = int(input())
sample = []
glevel = 0
for i in range(n):
    entry = input().split()
    sample.append((int(entry[0]), float(entry[1])) )
    
    # MY ORGINAL CODE THAT DOES THE SAME AS ABOVE
    # t,v = input().split()
    # t = int(t)
    # v = float(v) 
   # print(t,v)
    # sample.append(t)
    # sample.append(v)        
    
    # END OF MY CODE
    # print(sample)

for i in range(1,n):
    t2 = (sample[i][0]-sample[i-1][0])
    t1 = ((sample[i][1]+sample[i-1][1])/2) * t2
    glevel += t1

# ORIGNAL CODE I USED
# for i in range(1,n+1, 2):
#         # for i in range(n):
#             t2 = (sample[i+1]-sample[i-1])
#             t1 = ((sample[i]+sample[i+2])/2) * t2
#             # t1 = ((sample[i]+sample[i+2])/2)* (sample[i+1]-sample[i-1])
#             glevel += t1
# END OF ORIGINAL CODE

a = glevel/1000

print(a)

    
    
    
    
    
    
    
    
    
    # t1 = 0
        # t2 = (sample[3]+sample[5])/2 * (sample[4]-sample[2])
        # print(t2)
        # t3 = (t1 + t2)/1000
        # print(t3)
            
 
# t1 = (sample[1]+sample[3])/2 * (sample[2]-sample[0])
# print(t1)
# t2 = (sample[3]+sample[5])/2 * (sample[4]-sample[2])
# print(t2)
# t3 = (t1 + t2)/1000
# print(t3)
    
    # trap = (12+22)/2 *(3000-2000)
    # trapezoid = (2+12)/2 *(2000-1000)
    # print(trapezoid)
    # print(trap)