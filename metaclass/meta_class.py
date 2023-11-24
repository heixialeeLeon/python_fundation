class MyMetaClass(type):
    def __new__(*args):
        for i, item in enumerate(args):
            print(f'[{i}] {item}')
        return type.__new__(*args)

class MyBaseClass:
    pass

class MyClass(MyBaseClass, metaclass = MyMetaClass):
    var = 1
    def func(self):
        pass

print("******************************************************")

class UpperMetaClass(type):
    def __new__(meta, name, bases, dct):
        print('[1]', dct)

        upper_dct = {
            k if k.startswith("__") else k.upper(): v
            for k, v in dct.items()
        }
        return type.__new__(meta, name, bases, upper_dct)

    def __call__(cls):
        print("in the call")


class MyClass(metaclass=UpperMetaClass):
    var = 1

    def func(self):
        pass


print('[2]', MyClass.__dict__)
aa = MyClass()