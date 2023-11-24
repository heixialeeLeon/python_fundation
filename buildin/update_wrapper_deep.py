from functools import update_wrapper

def foo():
    print("this is foo")

def application(f):

    def wrapper(*args):
        print("this is wrapper")
        f(*args)
    return update_wrapper(wrapper, foo)

def application_2(f):
    def wrapper(*args):
        print("this is wrapper")
        f(*args)

    return wrapper

a = application(foo)
print(a.__name__)
print(a.__module__)
print(a.__annotations__)
print(a.__dict__)
print(a.__wrapped__)

print("*************************")
a = application_2(foo)
print(a.__name__)
print(a.__module__)
print(a.__annotations__)
print(a.__dict__)

print("************************")
a = foo
print(a.__name__)
print(a.__module__)
print(a.__annotations__)
print(a.__dict__)
