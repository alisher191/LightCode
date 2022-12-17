#3
'''
def sum(*args):
    a = 0
    for i in args:
        a = a + i
    print(a)
sum(56, 23, 25)
'''


#6
'''
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
print(square_digits(234))
'''
