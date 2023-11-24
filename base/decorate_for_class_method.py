import functools
import types

"""
函数修饰符的实现，用于修饰类方法
"""
def Context_Function(func):

    def proxy(instance,*args, **kwargs):
        print("call in proxy")
        return func(instance, *args, **kwargs)
    return proxy

class Foo(object):

    @Context_Function
    def hello(self):
        print("hello")

foo = Foo()
foo.hello()

print("************************************************")

"""
类修饰符的实现，用于修饰类方法
__get__() 的目的是创建一个绑定方法对象 (最终会给这个方法传递self参数)。
type.MethodType() 手动创建一个绑定方法来使用
"""
class Context_Class(object):
    def __init__(self, method):
        functools.update_wrapper(self, method)
        self.method = method

    def __call__(self, *args, **kwargs):
        print("call in __call__ of Context_Class")
        print("args is {},  kwargs is {}".format(args, kwargs))
        self.method(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            print("__get__ is called, instance is None")
            return self
        else:
            print("__get__ is called, instance is Not None")
            aa = types.MethodType(self, instance)
            """
            注意，这里是把instance[boo] 和 Context_Class这个描述符绑定
            所以其返回的bound method会直接调用__call__, 在__call__里再调用其修饰的函数
            """
            return types.MethodType(self, instance)

class Boo(object):

    @Context_Class
    def hello(self, word):
        print("hello: {}".format(word))

    def hello_another(self):
        print("hello another")
    hello_another_proxy = Context_Class(hello_another)

boo = Boo()
boo.hello("world")
boo.hello_another_proxy()

print("***********************************************")
"""
如果Context_Class修饰一个function, 由于不在类里面，所以不会调用到__get__方法
如果Context_Class修饰一个类的method, 则会调用到__get__ (因为函数也是一个描述符)
"""
print("to decroate a function will not trigger the __get__ method")
@Context_Class
def coo():
    print("call in coo")
coo()