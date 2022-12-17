# class Cat:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

    # def __len__(self):
    #     return len(self.name)
    # def __dir__(self):
    #     return ["name", "age", "breed"]
    #
#     def __str__(self):
#         return f"Name: {self.name}, \nAge: {self.age}, \nBreed: {self.breed}"
#
#
# a = Cat(age=2, name="Boo", breed="zxcv")
# print(a.__dict__)
# class Laptop:
# 	def __init__(self, processor, memory, card, disk, board, size):
# 		self.processor = processor
# 		self.memory = memory
# 		self.card = card
# 		self.disk  = disk
# 		self.board = board
# 		self.size = size
#
# 	def get_HP_info(self):
# 		print({
# 			"processor": self.processor,
# 			"memory": self.memory,
# 			"card": self.card,
# 			"disk": self.disk,
# 			"board": self.board,
# 			"size": self.size})
#
# l = Laptop("Intel", "8GB", "double", "500 mgb", "super size", "14 inch")
# l.get_HP_info()
# class Soda:
#     def __init__(self, ingredient):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None
#
#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'Газировка и {self.ingredient}')
#         else:
#             print('Обычная газировка')
#
#
# # Тесты
# drink1 = Soda(1)
# drink2 = Soda('малина')
# drink3 = Soda(5)
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()

class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'


# Тесты
triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())