'''
def rec(z):
    if len(z)==1 or len(z)==2:
        return z
    return z[0]+'('+ rec(z[1:-1])   + ")"+z[-1]
z = input()
print(rec(z))
'''
'''
tables = [lambda x = x: x*10 for x in range(1, 11)]
for i in tables:
    print(i())
'''
'''#1
def palindrom(x):
    s = x.lower()
    if len(s) < 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(x[1:-1])
print(palindrom(input()))
'''
#2
'''
def fact(x):
    if x == 1:
        return x
    return fact(x-1) * x
print(fact(4))
print(fact(5))
'''
'''
def rec(x):
    if x < 0:
        return 0
    elif x < 10:
        print(x)

        rec(x+1)
        print(x)
rec(int(input()))
'''
'''
# Рекурсивная функция - возвращает сумму чисел во входящем наборе
L = [ 2, 3, 8, 11, 4, 6 ]
a = []
def asd(a):
    if a == []:
        return 0
    else:
        summ = asd(a[1:])
        summ = summ + a[0]
        return summ

summ = asd(L)
print('summ = ', summ)
'''
'''
a = [1,45,65,[45,[78,98], 78], 789]
def rec(lst, level=1):
    print(*lst, 'level=', level)
    for i in lst:
        if type(i)==list:
            rec(i, level+1)
rec(a)
'''
