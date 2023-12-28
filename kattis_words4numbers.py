# https://open.kattis.com/problems/wordsfornumbers

numberList ={
    "0":"zero",
    "1":"one",
    '2':"two",
    '3':"three",
    '4':"four",
    '5':"five",
    '6':"six",
    '7':"seven",
    '8':"eight",
    '9':"nine",
    '10':"ten",
    '11':"eleven",
    '12':"twelve",
    '13':"thirteen",
    '14':"fourteen",
    '15':"fifteen",
    '16':"sixteen",
    '17':"seventeen",
    '18':"eighteen",
    '19':"nineteen",
    '20':"twenty",
    '21':"twenty-one",
    '22':"twenty-two",
    '23':"twenty-three",
    '24':"twenty-four",
    '25':"twenty-five",
    '26':"twenty-six",
    '27':"twenty-seven",
    '28':"twenty-eight",
    '29':"twenty-nine",
    '30':"thirty",
    '31':"thirty-one",
    '32':"thirty-two",
    '33':"thirty-three",
    '34':"thirty-four",
    '35':"thirty-five",
    '36':"thirty-six",
    '37':"thirty-seven",
    '38':"thirty-eight",
    '39':"thirty-nine",
    "40":"forty",
    '41':"forty-one",
    '42':"forty-two",
    '43':"forty-three",
    '44':"forty-four",
    '45':"forty-five",
    '46':"forty-six",
    '47':"forty-seven",
    '48':"forty-eight",
    '49':"forty-nine",
    '50':"fifty",
    '51':"fifty-one",
    '52':"fifty-two",
    '53':"fifty-three",
    '54':"fifty-four",
    '55':"fifty-five",
    '56':"fifty-six",
    '57':"fifty-seven",
    '58':"fifty-eight",
    '59':"fifty-nine",
    '60':"sixty",
    '61':"sixty-one",
    '62':"sixty-two",
    '63':"sixty-three",
    '64':"sixty-four",
    '65':"sixty-five",
    '66':"sixty-six",
    '67':"sixty-seven",
    '68':"sixty-eight",
    '69':"sixty-nine",
    '70':"seventy",
    '71':"seventy-one",
    '72':"seventy-two",
    '73':"seventy-three",
    '74':"seventy-four",
    '75':"seventy-five",
    '76':"seventy-six",
    '77':"seventy-seven",
    '78':"seventy-eight",
    "79":"seventy-nine",
    '80':"eighty",
    "81":"eighty-one",
    "82":"eighty-two",
    "83":"eighty-three",
    "84":"eighty-four",
    "85":"eighty-five",
    "86":"eighty-six",
    "87":"eighty-seven",
    "88":"eighty-eight",
    "89":"eighty-nine",
    "90":"ninety",
    "91":"ninety-one",
    "92":"ninety-two",
    "93":"ninety-three",
    "94":"ninety-four",
    "95":"ninety-five",
    "96":"ninety-six",
    "97":"ninety-seven",
    "98":"ninety-eight",
    "99":"ninety-nine",
    }
def num4words():
    while True:
        n = input().split(" ")
        #n = n.split()
        print(n)
        # newSen = []
        newSen1 = ""
        firstNum = ""
        hold = ""
        # x = ""
        for i in range(len(n)):
            hold = n[i]
            y = hold[0:-1]
            if y.isdigit():
                y = int(y)
                if y > 9:
                    y = str(y)
                    firstNum = number.get(y)
                    newSen1 += firstNum
                    if "," in n[i][-1]:    
                        newSen1 += "," + " "
                    elif "." in n[i][-1]:
                        newSen1 += "." + " "
                    continue
            elif n[i]in number.keys():
                hold = n[i]
                f = n[i-1]
                if hold in number.keys() and n[i] == n[0]:        
                    firstNum = number.get(hold)
                    firstNum = firstNum.capitalize()
                    newSen1 += firstNum + " "
                elif hold in number.keys() and "." in f or "!" in f or "?" in f or "\n" in f:
                    firstNum = number.get(hold)
                    firstNum = firstNum.capitalize()
                    newSen1 += firstNum 
                elif hold in number.keys():
                    newSen1 += firstNum
            else:
                newSen1 += n[i] + " "
        print(newSen1)
num4words()

# def num4words():
#     while True:
#         n = input()
#         n = n.split()
#         # newSen = []
#         newSen1 = ""
#         firstNum = ""
#         hold = ""
#         # x = ""
#         for i in range(len(n)):
#             hold = n[i]
#             y = hold[0:-1]
#             if y.isdigit():
#                 y = int(y)
#                 if y > 9:
#                     y = str(y)
#                     firstNum = number.get(y)
#                     newSen1 += firstNum
#                     if "," in n[i][-1]:    
#                         newSen1 += "," + " "
#                     elif "." in n[i][-1]:
#                         newSen1 += "." + " "
#                     continue
#             elif n[i]in number.keys():
#                 hold = n[i]
#                 f = n[i-1]
#                 if hold in number.keys() and n[i] == n[0]:        
#                     firstNum = number.get(hold)
#                     firstNum = firstNum.capitalize()
#                     newSen1 += firstNum + " "
#                 elif hold in number.keys() and "." in f or "!" in f or "?" in f or "\n" in f:
#                     firstNum = number.get(hold)
#                     firstNum = firstNum.capitalize()
#                     newSen1 += firstNum 
#                 elif hold in number.keys():
#                     newSen1 += firstNum
#             else:
#                 newSen1 += n[i] + " "
#         print(newSen1)
# num4words()

# This works below realy well.
# while True:
#     n = input()
#     n = n.split()
#     newSen = []
#     newSen1 = ""
#     firstNum = ""
#     hold = ""
#     x = ""
#     for i in range(len(n)):
#         hold = n[i]
#         y = n[i][0:-1]
#         if y.isdigit():
#             y = int(y)
#             if y > 9:
#                 y = str(y)
#                 firstNum = number.get(y)
#                 newSen1 += firstNum
#                 if "," in n[i][-1]:    
#                     newSen1 += "," + " "
#                 elif "." in n[i][-1]:
#                     newSen1 += "." + " "
#                 continue
#         if n[i]in number.keys():
#             hold = n[i]
#             f = n[i-1]
#             if hold in number.keys() and n[i] == n[0]:        
#                 firstNum = number.get(hold)
#                 firstNum = firstNum.capitalize()
#                 newSen1 += firstNum + " "
#             elif hold in number.keys() and "." in f or "!" in f or "?" in f or "\n" in f:
#                 firstNum = number.get(hold)
#                 firstNum = firstNum.capitalize()
#                 newSen1 += firstNum 
#             elif hold in number.keys():
#                 newSen1 += firstNum
#         else:
#             newSen1 += n[i] + " "
#     print(newSen1)





# for i in range(1):
#     print(newSen1)
#     x += newSen1[i]+ " "
# print(x)
# print(newSen, x)

# 99 The speed limit is 40, mph, but you were going over 65. 56


# n = input().split()
# def uniqueChar(n):
#     # n = n.split()
#     # f = n[i-1]
#     newSen = ""
#     firstNum = ""
#     hold = ""
#     for i in range(len(n)):
#         if n[i]in number.keys():
#             # print("theres a number here")
#             hold = n[i]
#             f = n[i-1]
#             if hold in number.keys() and n[i] == n[0]:        
#             # if hold == n[0]:
#                 # number.values().capitalize()
#                 firstNum = number.get(hold)
#                 # print(firstNum)
#                 firstNum = firstNum.capitalize()
#                 # print(firstNum)
#                 # newSen + firstNum.capitalize()
#                 newSen += firstNum + " "
#             elif hold in number.keys() and "." in f or "!" in f or "?" in f or "\n" in f:
#                 firstNum = number.get(hold)
#                 firstNum = firstNum.capitalize()
#                 newSen += firstNum + " "
#                 # print("There is a periof here")
#             elif hold in number.keys():
#                 newSen += number.get(n[i]) + " "
#         else:
#             newSen += n[i] + " "
#     return newSen
        
        
# print(uniqueChar(n))


# n = input()
# def uniqueChar(n):
#     n = n.split()
#     newSen = []
#     firstNum = ""
#     hold = ""
#     x = ""
#     for i in range(len(n)):
#         hold = n[i]
#         y = n[i][0:-1]
#         if y.isdigit():
#             print(y)
#             y = int(y)
#             if y > 9:
#                 y = str(y)
#                 firstNum = number.get(y)
#                 newSen.append(firstNum)
#                 newSen.append(",")
#         if n[i] in number.keys():
#             # print("theres 60a number here")
#             hold = n[i]
#             f = n[i-1]
#             if hold.isdigit() and hold in number.keys() and n[i] == n[0]:        
#             # if hold == n[0]:
#                 # number.values().capitalize()
#                 firstNum = number.get(hold)
#                 # print(firstNum)
#                 firstNum = firstNum.capitalize()
#                 # print(firstNum)
#                 # newSen + firstNum.capitalize()
#                 newSen.append(firstNum)
#             elif hold in number.keys() and "." in f or "!" in f or "?" in f or "\n" in f:
#                 firstNum = number.get(hold)
#                 firstNum = firstNum.capitalize()
#                 newSen.append(firstNum)
#                 # print("There is a periof here")
#             elif hold in number.keys():
#                 firstNum= number.get(hold)
#                 newSen.append(firstNum)
#             # elif n[i[0:-1]] in number.keys():
#             #     firstNum = number.get(hold)
#             #     newSen.append(firstNum)
#         else:
#             newSen.append(n[i])
#     for i in range(len(n)):
#         x += newSen[i] + " "
#     return  x
#     # print(newSen)
        
        
# print(uniqueChar(n))


    