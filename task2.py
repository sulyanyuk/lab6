from random import *

class Team:

    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score

teamList1 = []
teamList2 = []

for i in range(0,24):
    if i <12:
        teamList1.append(Team(f"name{i+1}",1,0))
    else:
        teamList2.append(Team(f"name{i+1}", 2, 0))

for i in range(0,11):
    ### Group 1
    result = randint(1,3) ### 1 - 1st team win, 2 - second team win, 3 - draw
    if result == 1:
        teamList1[i].score += 3
    if result == 2:
        teamList1[i+1].score += 3
    if result == 3:
        teamList1[i].score += 1
        teamList1[i+1].score += 1

     ### Group 2
    result = randint(1,3) ### 1 - 1st team win, 2 - second team win, 3 - draw
    if result == 1:
        teamList2[i].score += 3
    if result == 2:
        teamList2[i+1].score += 3
    if result == 3:
        teamList2[i].score += 1
        teamList2[i+1].score += 1

j = 0 ### Bubble Sort
while True:
    noSwap1 = True
    noSwap2 = True
    for i in range(0,12-1):
        if teamList1[i].score < teamList1[i+1].score:
            teamList1[i],teamList1[i+1] = teamList1[i+1],teamList1[i]
            noSwap1 = False
        if teamList2[i].score < teamList2[i+1].score:
            teamList2[i],teamList2[i+1] = teamList2[i+1],teamList2[i]
            noSwap2 = False
    j += 1
    if noSwap1 and noSwap2:
        break
teamList1 = teamList1[:6]
teamList2 = teamList2[:6]

print("group 1:")
for team in teamList1:
    print(team.name,team.score)
print("")
print("group 2:")
for team in teamList2:
    print(team.name,team.score)