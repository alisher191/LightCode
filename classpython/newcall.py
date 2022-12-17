class Call:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, *args, **kwargs):  # Реализует вызов экземпляра
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой!")

        return args[0].strip(self.arg)


C = Call("1234567890")
res = C("0Hello world!2")
print(res)


class New:
    def __new__(cls, *args, **kwargs): #
        print("__new__")
        super().__new__(cls)

    def __init__(self):
        pass