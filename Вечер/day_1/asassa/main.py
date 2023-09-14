# import random

# students = ["Nurik", "Aktilek", "Uluk", "Elvira", "Mura", "Alim"]
# random.shuffle(students)

# problems = [i for i in range(1, 23)]
# random.shuffle(problems)

# team_A = []
# team_B = []


# for problem in problems:
#     if len(team_A) < 11:
#         team_A.append(problem)
#     elif len(team_B) < 11:
#         team_B.append(problem)

# print(f"Команда А: {team_A}")
# print(f"Команда B: {team_B}")

with open('test.txt', 'w') as file:
    file.write(str([i for i in range(10)]))

with open('test.txt', 'r') as file:
    das = str(file.read())
    print(das)