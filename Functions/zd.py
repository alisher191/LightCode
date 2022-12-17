a = [1,45,65,[45,[78,98], 78], 789]
def rec(lst, level=1):
    print(*lst, 'level=', level)
    for i in lst:
        if type(i)==list:
            rec(i, level+1)
rec(a)

'''
import time

def decor(fun):
    def wrapper():
        start_time = time.time()
        fun()
        print(time.time() - start_time)
    return wrapper
@decor
def pr():
    print("Оборачиваемая функция")
pr()

#m = decor(pr)
#m()
'''
'''
def rec(x):
    if x < 10:
        print(x)
        rec(x + 1)
        #print(x)
rec(0)
'''
'''
def sd(x):
    return x**2
print(sd(5))

print((lambda x: x**2)(5))
'''
