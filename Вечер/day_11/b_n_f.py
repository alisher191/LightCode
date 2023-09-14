# Built in functions

# bool()
# int()
# float()
# list()
# tuple()
# set()
# dict()
# str()

# print()
# input()

# min()
# max()
# len()
# range()

# reversed()
# abs()
# all()
# any()
# bin()
# callable()
# chr()
# divmod(a, b) -> (a // b, a % b)
# enumerate([])
# print(eval('1+2')) -> 3

# filter()
"""
Когда None используется в качестве первого аргумента функции filter(), 
извлекаются все элементы, которые являются истинными значениями 
(дает True при преобразовании в логическое).
# """
# random_list = [1, 'a', 0, False, True, 213]
# filtered_list = list(filter(None, random_list))
# print(filtered_list)

# map()
# l = ['mat', 'sat', 'bat', 'cat']
# t = list(map(list, l))
# print(t)
# t = []
# for i in l:
#     t.append(list(i))
# print(t)

# sorted()
# print(sorted([2, 5, 6, 3, 4, 1]))

# sum()
# type()

# zip()

a = [1, 4, 7, 8, 9]
b = [2, 5, 8, 90]
c = [3, 6, 9]

d = list(zip(a, b, c))

for i in d:
    print(i)
