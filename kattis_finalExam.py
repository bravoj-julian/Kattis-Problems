# https://open.kattis.com/problems/finalexam2

x = int(input())
hanhAnswer = []
correctAnswer = []
correct = 0
for i in range(x):
    a = input().upper()
    correctAnswer.append(a)
    if i ==0:
        continue
    else:
        hanhAnswer.append(a)
for i in range(len(hanhAnswer)):
    if hanhAnswer[i] == correctAnswer[i]:
        correct +=1
# print(hanhAnswer)
# print(correctAnswer)
print(correct)