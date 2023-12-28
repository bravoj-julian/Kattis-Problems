# https://open.kattis.com/problems/ratingproblems

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