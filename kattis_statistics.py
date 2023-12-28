# https://open.kattis.com/problems/statistics

# https://docs.python.org/3/library/exceptions.html

# case = 0
# while True:
#     dataCASE, *entry = list(map(int,input().split()))
#     l = entry[0] 
# # print(entry)
#     # entry.remove(entry[0])
#     print(entry)
# # print(entry)
#     maxVal = max(entry)
#     minVal = min(entry)
#     rangeVal = maxVal - minVal
#     case += 1
# # print(maxVal)
# # print(l)
#     # print('Case',str(case)+':',minVal, maxVal, rangeVal)
#     print("Case {}: {} {} {}".format(case,minVal,maxVal,rangeVal))
 
# exception EOFError
# Raised when the input() function hits an end-of-file condition (EOF) without reading any data. (N.B.: the io.IOBase.read() and io.IOBase.readline() methods return an empty string when they hit EOF.)


case = 0
while True:
    try:
        dataCASE, *entry = list(map(int,input().split()))
    except  EOFError:
        break
    
    maxVal = max(entry)
    minVal = min(entry)
    rangeVal = maxVal - minVal
    case += 1
    print('Case',str(case)+':',minVal, maxVal, rangeVal)
    # print("Case {}: {} {} {}".format(case,minVal,maxVal,rangeVal))