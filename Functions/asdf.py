
a = [25, 36, 789, [123, 465, 78, [45, 78, 56, 12], 79, 8], 256, 4654, 78]

def unpack(lst, level=0):
    print(*lst, 'level=', level)
    for i in lst:
        if type(i) == list:
            unpack(i, level-1)
unpack(a)

'''
import time

def decor(func):
    def wrapper():
        starttime = time.time()
        func()
        print(time.time() - starttime)
    return wrapper
'''
'''
print((lambda x: x**2)(5))
'''
'''
@decor
def fun():
    print("Mid")
fun()

@decor
def rec(x):
    if x < 10:
        print(x)
        rec(x+1)
        print(x)
rec(1)
'''
#1->2->3->4->5->n->9  9->n->5->4->3->2->1

'''
def sum1(name, **a):
    print(f'Pets owner: {name}')
    for key, value in a.items():
        print(f"{key}'s name -->  {value}") 
sum1("Mike", dog="Alex", turtle="Leo", fish=["Dori", "Nemo"])
'''
