class MyClass(object):
    pass

print("custom define class is instance of type")
print(isinstance(MyClass,type))
print(issubclass(MyClass,type))

print("custome defin class is both instance and subclass of object")
print(isinstance(MyClass,object))
print(issubclass(MyClass,object))

print("type is instance and subclass of object")
print(isinstance(type,object))
print(issubclass(type,object))

print("object is instance of type, but is to root class")
print(isinstance(object,type))
print(issubclass(object,type))