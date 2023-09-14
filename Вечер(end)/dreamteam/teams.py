import random


students = ['Erkin', 'Askar', 'Edil', 'Cholponai', 'Ikram', 'Alexey', 'Evgeniy']
random.shuffle(students)

for student in range(len(students)):
    print(student+1, students[student])

# teams = {
#     "Fire": [],
#     "Water": [],
#     "Tree": [],
#     "Metal": [],
#     "Earth": []
# }


# problem = "Cпарсить данные с сайта онлайн магазина и добавить его продукты (вместе с названием, описанием, ценой и ссылкой на сам товар и фото) в бота.\n\n"
#
#
# for student in students:
#     if len(teams['Fire']) < 2:
#         teams['Fire'].append(student)
#     elif len(teams['Water']) < 2:
#         teams['Water'].append(student)
#     elif len(teams['Tree']) < 2:
#         teams['Tree'].append(student)
#     elif len(teams['Metal']) < 2:
#         teams['Metal'].append(student)
#     elif len(teams['Earth']) < 2:
#         teams['Earth'].append(student)
#
# with open('dreamteam.txt', 'w') as drt:
#     drt.write(problem)
#     drt.write(str(teams))
