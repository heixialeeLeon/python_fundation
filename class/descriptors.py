class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving ',self.name)
        return self.val

    def __set__(self, obj, objtype):
        print("Updating ", self.name)
        self.val =obj


class MyClass(object):
    x = RevealAccess(10,"var x")
    var = "abc"

    def __init__(self):
        self.instance_var = 0

    def func(self):
        pass

    @property
    def p_val(self):
        return self.instance_var

m = MyClass()
m.x
m.x =20
print(hasattr(MyClass,"func"))
print(hasattr(MyClass,"p_val"))
print("**************************************")
print("MyClass instance dict: ", m.__dict__)
print("MyClass dict: ", MyClass.__dict__)

def func():
    pass
print("func __get__ and __set__ method")
print("function: ")
print(hasattr(func,'__get__'))
print(hasattr(func,'__set__'))
print("class function: ")
print(hasattr(MyClass.func,'__get__'))
print(hasattr(MyClass.func,'__set__'))
print("instance_var:")
print(hasattr(m.instance_var,'__get__'))
print(hasattr(m.instance_var,'__set__'))
print("MyClass.p_val:")
print(hasattr(MyClass.p_val,'__get__'))
print(hasattr(MyClass.p_val,'__set__'))
print(m.__dict__)
print(dir(m))
# class Student:
#     def __init__(self):
#         self.name=''
#         self.age=0
#
# student = Student()
# print(student.__dict__)
# print(dir(student))