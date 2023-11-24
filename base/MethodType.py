import types

"""
为对象动态绑定方法
"""

class Foo(object):
    def __init__(self):
        pass

    def abc(self):
        print("call in abc")

def func(*args, **kwargs):
    print("call in the func")
    print("args: {},  kwargs: {}".format(args, kwargs))

print("the parameters of a function object:")
foo = Foo()
foo.func = func
foo.func("hello")

"""
通过MethodType,将会生产一个bind method
当调用一个bind method，默认会传与其bind的instance作为第一个参数
"""
print("*******************************************")
print("the parameters of a method:")
foo.func_bind = types.MethodType(func, foo)
foo.func_bind("hello")

print("*******************************************")
print("the function type is as follows: ")
print("the type of func of foo is {}".format(type(foo.func)))
print("the type of func of foo_bind is {}".format(type(foo.func_bind)))
print("the type of func of abc is {}".format(type(foo.abc)))
