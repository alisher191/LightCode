import random

st = ['Alim', 'Aktilek', 'Elvira', 'Meder', 'Nurik', 'Uluk']
random.shuffle(st)

teamA = []
teamB = []

for s in st:
    if len(teamA) < 3:
        teamA.append(s)
    elif len(teamB) < 3:
        teamB.append(s)

print(f"TeamA: {teamA}")
print(f"TeamB: {teamB}")
