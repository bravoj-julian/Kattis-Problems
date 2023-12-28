# https://open.kattis.com/problems/pieceofcake2


def pieceCake():
    n, h, v = input().split()
    n = int(n) #length of the side of square
    h = int(h) # horizontal distance from cut
    v = int(v) # vertical distance from cut
    nh = n - h
    nv = n - v 
    volume = (4 * nh * nv, 4 * h * v, 4 * h * nv, 4 * nh * v)
    x = sorted(volume, reverse = True)
    return x[0]
print(pieceCake())