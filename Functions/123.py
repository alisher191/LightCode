'''
def owner(name, **kwargs):
    print(f"Owners name: {name}!")
    for key, value in kwargs.items():
        print(f"{key}'s name is {value}")
owner(name='Altay', dog='Alex', fish=['Dori', 'Nemo'], turtle='Leo')
'''

'''
def fun(*int1):
    a = 0
    for i in int1:
        a = a + i
    print(a)
fun(12, 25, 56, 236, 456)
'''
'''
def rang(min, max):
    ranger_list = range(min, max+1)
    return ranger_list
print(rang(max=5, min=1))
'''
'''
def f(m, g=9.8):
    return m * g
print(f(m=75,g=3))
'''
