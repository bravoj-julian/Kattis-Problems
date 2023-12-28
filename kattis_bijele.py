#https://open.kattis.com/problems/bijele

k,q,r,b,kn,p = input().split()
king = 1
queen = 1
rooks = 2
bishops = 2
knights = 2
pawns = 8
kdiff = king - int(k)
qdiff = queen - int(q)
rdiff = rooks - int(r)
bdiff = bishops - int(b)
kndiff = knights - int(kn)
pdiff = pawns - int(p)
print( kdiff, qdiff, rdiff, bdiff, kndiff, pdiff)


# k,q,r,b,kn,p = input().split()
# # print(k,q,r,b,kn,p)
# king = 1
# queen = 1
# rooks = 2
# bishops = 2
# knights = 2
# pawns = 8
# # chestPieces = [1,1,2,2,2,8]
# # requiredPieces = ""
# def checkP(k,q,r,b,kn,p):
#     kdiff = king - int(k)
#     # requiredPieces + str(kdiff)
#     # requiredPieces = requiredPieces + str(kdiff)
#     # print(kdiff)  
#     qdiff = queen - int(q)
#     # requiredPieces + str(qdiff) +" "
#     # print(qdiff)  
#     rdiff = rooks - int(r)
#     # requiredPieces + str(rdiff) +" "
#     # print(rdiff)  
#     bdiff = bishops - int(b)
#     # requiredPieces + str(bdiff) +" "
#     # print(bdiff)  
#     kndiff = knights - int(kn)
#     # requiredPieces + str(kndiff) +" "
#     # print(kndiff)  
#     pdiff = pawns - int(p)
#     # requiredPieces + str(pdiff) + " "
#     # print(pdiff)  
#     # print(requiredPieces)
#     a = print( kdiff, qdiff, rdiff, bdiff, kndiff, pdiff)
#     return a
# print(checkP(k,q,r,b,kn,p))

# k = int(input())
# kdiff = king - int(k)
# print(kdiff)  
# # p = int(input())
# pdiff = pawns - int(p)
# print(pdiff)

# def checkPiece(onHandPiece):
#     for i in range(1):
#         x = int(chestPieces[i]) - int(onHandPiece[i])
#         requiredPieces + x

# print(checkPiece(onHandPiece))