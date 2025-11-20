# Ramesh partner selection program

N = int(input())        # number of people
X = int(input())        # minimum required skill

partners = []           # list to store selected partners

for _ in range(N):
    Y = int(input())    # skill of each person
    if Y >= X:
        partners.append(Y)

# Output selected partners
if len(partners) == 0:
    print("No Partners Found")
else:
    for skill in partners:
        print(skill)
