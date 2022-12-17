# class Computer:
#     def __init__(self, computer, ram, ssd):
#         self.computer = computer
#         self.ram = ram
#         self.ssd = ssd
#
#
# class Laptop(Computer):
#     def __init__(self, computer, ram, ssd, model):
#         super().__init__(computer, ram, ssd)
#         self.model = model
#
#
# lenovo = Laptop('lenovo', 2, 512, 'l420')
#
# print('This computer is:', lenovo.computer)
# print('This computer has ram of', lenovo.ram)
# print('This computer has ssd of', lenovo.ssd)
# print('This computer has this model:', lenovo.model)
#

# # # Задача 1
# class Factory:
#     def engine(self):
#         return "Двигатель создан"
#
#     def bridge(self):
#         return "Ходовая часть создана"
#
#
# class Toyota(Factory):
#     def wheels(self):
#         return "Колёса готовы"
#
#     def windows(self):
#         return "Стёкла готовы"
#
#
# auto = Toyota()
# print(auto.wheels())
# print(auto.windows())
# print(auto.bridge())
# print(auto.engine())
#
# lst = [auto.wheels(), auto.windows(), auto.bridge(), auto.engine()]
# print(lst)
# # Задача 2
#
#
# class Zoo:
#     def __init__(self):
#         self.animal_1 = "Тигр"
#         self.animal_2 = "Бегемот"
#         self.animal_3 = "Жираф"
#
#
# z = Zoo()
# print(z)
# print(z.animal_1)
# z.animal_1 = "Лев"
# print(z.animal_1)
# z.animal_4 = [z.animal_2, z.animal_3]
# print(z.animal_4)
# print(z.animal_3)
# z.animal_3 = "Змея"
# print(z.animal_3)
#
# #
# class Employee:
#     salary = 0
#     count = 0
#
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#
#     def add_salary(self, a):
#         self.salary += a
#         return f'{self.name} получает прибавку в размере {a} {Employee.salary}'
#
#     def full_name(self):
#         return f'full name: {self.name} {self.last_name}'
#
#
# per1 = Employee('John', 'Snow')
# per2 = Employee('Sam', 'Smit')
# per2.add_salary(100)
# print(per1.add_salary(1000))
# print(per1.salary)
# print(per2.salary)
