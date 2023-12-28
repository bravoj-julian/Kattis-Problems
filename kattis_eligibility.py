# https://open.kattis.com/problems/eligibility

n = int(input())
x = ''
for i in range(n):
    entry = input().split()
    name = entry[0]
    startEdu = entry[1]
    sEdu = startEdu.split('/')
    year = int(sEdu[0])
    dob = entry[2]
    sdob = dob.split('/')
    dobYear = int(sdob[0])
    courses = int(entry[3])
    if year >= 2010:
        x = 'eligible'
    elif dobYear >= 1991:
        x = 'eligible'
    elif courses <= 40:
        x = "coach petitions"
    else:
        x = 'ineligible'
    print(name,x)
    # print(name, year, dobYear, courses)