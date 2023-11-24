class MyClass(object):
    _private_one = 0
    __private_two =1

# with the _ start variable not rename
print("_private_one: ",hasattr(MyClass,'_private_one'))
# with the __ start variable rename
print("__private_two: ",hasattr(MyClass,'__private_two'))
print("_MyClass__private_two: ",hasattr(MyClass,'_MyClass__private_two'))
print(dir(MyClass))