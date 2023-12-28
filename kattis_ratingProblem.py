# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:52:29 2022

@author: danger bravo
"""

# n,k = input().split()
# n = int(n)
# k = int(k)
# def ratingJudge(n,k):
#     remainJudge = n - k
#     judgeScore = 0
#     maxScore = 0
#     minScore = 0
#     for i in range(k):
#         r = int(input())
#         judgeScore += r
#         maxScore = ((remainJudge * 3) + judgeScore) / n
#         return 
#         minScore = ((remainJudge * -3) + judgeScore) / n
# # print(judgeScore)
# # print(minScore, maxScore)
#     score = float(minScore), float(maxScore)
#     # return minScore, maxScore, 
#     return score
# print(ratingJudge(n,k))



#THIS CODE WORKS BELOW
n,k = input().split()
n = int(n)
k = int(k)
remainJudge = n - k
judgeScore = 0
maxScore = 0
minScore = 0
maxScore = ((remainJudge * 3) + judgeScore) / n
minScore = ((remainJudge * -3) + judgeScore) / n
for i in range(k):
    r = int(input())
    judgeScore += r
    maxScore = ((remainJudge * 3) + judgeScore) / n
    minScore = ((remainJudge * -3) + judgeScore) / n
    
# print(judgeScore)
# print(minScore, maxScore)
score = float(minScore), float(maxScore)
    # return minScore, maxScore, 
print(float(minScore), float(maxScore))