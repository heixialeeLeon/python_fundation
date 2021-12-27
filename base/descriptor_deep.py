"""
描述符的属性是定义在类的属性里面的，不能定义在instance的属性，即不定义在__init__()函数中

当找一个属性时，先check该属性是否是类属性是否是一个descriptor, 如果是，则调用其__get__()方法

当一个instance属性和non-data描述符重名时候，先调用instance属性，如果失败，再查找描述符
当一个instance属性和data描述符重名时候，先调用data描述符
"""

class NonData_Destriptor(object):
    def __init__(self, default = "student"):
        self.name = default

    def __get__(self, instance, owner):
        print("call in NonData_Destriptor __get__")
        return self.name

class Data_Destriptor(object):
    def __init__(self, default = "student"):
        self.name = default

    def __get__(self, instance, owner):
        print("call in Data_Destriptor __get__")
        return self.name

    def __set__(self, instance, value):
        pass

class Student(object):
    name = NonData_Destriptor()
    test = NonData_Destriptor()

    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        print("call in Student.__getattribute__")
        return super().__getattribute__(item)

class Student_2(object):
    name = Data_Destriptor()

    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        print("call in Student.__getattribute__")
        return super().__getattribute__(item)

print("instance 属性和 Non_data descriptor 重名")
s1 = Student("Miki")
print(s1.name)
print("描述符如何被调用")
print(s1.test)
print("instance 属性和 data descriptor 重名")
s2 = Student_2("Miki")
print(s2.name)