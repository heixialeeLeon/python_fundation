from abc import ABCMeta
"""
The build in function show
"""
class A(object):
    def __init__(self):
        pass

print("The class inherit from the object ***********************")
print("the base class is {}".format(A.__base__))
print("the module is {}".format(A.__module__))
print("the type is {}".format(A.__class__))
print("the attributes is {}".format(A.__dict__))
print("the doc is {}".format(A.__doc__))
print("")

class AA(metaclass=ABCMeta):
    def __init__(self):
        pass
print("The class inherit from the ABCMeta ***********************")
print("the base class is {}".format(AA.__base__))
print("the module is {}".format(AA.__module__))
print("the type is {}".format(AA.__class__))
print("the attributes is {}".format(AA.__dict__))
print("the doc is {}".format(AA.__doc__))
print("")

print("The float buildin class ***********************")
print("the base class is {}".format(float.__base__))
print("the module is {}".format(float.__module__))
print("the type is {}".format(float.__class__))
print("the attributes is {}".format(float.__dict__))
print("the doc is {}".format(float.__doc__))