class mystaticmethod:
    def __init__(self, func):
        print("call in mystaticmethod __init__")
        self.func = func

    def __get__(self, instance, onwer):
        return self.func


class Foo:

    @mystaticmethod
    def add(a, b):
        return a+b

    def add_2(a, b):
        return a+b

foo = Foo()
print(foo.add)
print(foo.add_2)
print(Foo.add(2,4))
print(foo.add(2,4))
print(Foo.add_2(2,2))
print(foo.add_2(2,2))