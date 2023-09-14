# class ClassName:
#     def __new__(cls, *args, **kwargs):
#         print('1. Создается новый экземпляр класса.')
#         return super().__new__(cls)
    
#     def __init__(self, a) -> None:
#         print('2. Работает Init')
#         self.a = a
        
# a = ClassName(12)
# a


class ClassName:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassName, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, a) -> None:
        print('2. Работает Init')
        self.a = a
        
a = ClassName(12)
a
