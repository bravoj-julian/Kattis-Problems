# https://open.kattis.com/problems/provincesandgold


g,s,c = input().split()
gold = 3
silver = 2
copper = 1
def province(g,s,c):
    g = int(g) * gold
    s = int(s) * silver
    c = int(c) * copper
    buyingPower = g + s + c
    maxCardT = ""
    maxCardC = ""
    cardsT = [["Province" , 8],["Duchy" , 5],["Estate" , 2]]
    cardsC = [["Gold" , 6],["Silver" , 3],["Copper" , 0]]
    for i in range(len(cardsT)):
        if buyingPower >= (cardsT[i][1]):
            maxCardT = cardsT[i][0]
            break 
    for i in range(len(cardsC)):        
        if buyingPower >= (cardsC[i][1]):
            maxCardC = cardsC[i][0]
            break
    if maxCardT == "":
        maxCards = maxCardC
    else:
           maxCards = maxCardT+ " or " + maxCardC
    return maxCards
print(province(g, s, c))


g,s,c = input().split()
gold = 3
silver = 2
copper = 1
def province(g,s,c):
    g = int(g) * gold
    s = int(s) * silver
    c = int(c) * copper
    buyingPower = g + s + c
# print(buyingPower)
    maxCardT = ""
    maxCardC = ""
    cardsT = [["Province" , 8],["Duchy" , 5],["Estate" , 2]]
    cardsC = [["Gold" , 6],["Silver" , 3],["Copper" , 0]]
# print(cards)
    for i in range(len(cardsT)):
        if buyingPower >= (cardsT[i][1]):
        # print(cardsT[i][0])
            maxCardT = cardsT[i][0]
        # maxCardT = max(cardsT[:])
            # print(maxCardT)
            break 
    # return maxCardT
    for i in range(len(cardsC)):        
        if buyingPower >= (cardsC[i][1]):
        # maxCardC = max(cardsC)
        # print(cardsC[i][0])
            maxCardC = cardsC[i][0]
            # print(maxCardC)
        # print(maxCard[0][0])
            break
    if maxCardT == "":
        maxCards = maxCardC
    else:
           maxCards = maxCardT+ " or " + maxCardC
    return maxCards
print(province(g, s, c))
