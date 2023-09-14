s = input()
print(max(map(lambda x: (s.count(x), x), s))[1])

# sumb = ''
# c_sumb = 0
# dct = {}
# for i in s:
#     if i not in dct:
#         dct[i] = 0
#     dct[i] += 1
# for key in dct:
#     if dct[key] < c_sumb:
#         c_sumb = dct[key]
#         sumb = key
# print(sumb)
