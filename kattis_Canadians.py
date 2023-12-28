# https://open.kattis.com/problems/canadianseh
spyTalk = input()
canada = "eh?"
# print(spyTalk[-1-2:])
if canada in spyTalk[-1-2:]:
    print("Canadian!")
else:
    print('Imposter!')