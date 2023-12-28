# https://open.kattis.com/problems/pyramids
blocks = int(input())

pyramid = 1
pblocks = 0
height = 0
while blocks >= pblocks:
    pblocks += pyramid * pyramid
    pyramid += 2
    if pblocks > blocks:
        break
    height +=1
    # print(pblocks, pyramid, height)
print(height)
    
