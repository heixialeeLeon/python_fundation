"""
定义函数的时候
*args：表示的就是将实参中按照位置传值，多出来的值都给args，且以元组的方式呈现，
**kwargs：表示的就是形参中按照关键字传值把多余的传值以字典的方式呈现

当传入参数的时候
*() 解开元组
**{} 解开字典
"""

print("The usage of '*' :")
def foo(x, *args):
    print("x: {}".format(x))
    print("args: {}".format(args))

foo(1,2,3,4)
foo(0)
foo((1,2,3,4))
foo(*(1,2,3,4))

print("******************************************")
print("The usage of '**' :")

def foo(x, **kwargs):
    print("x: {}".format(x))
    print("kwargs: {}".format(kwargs))

foo(1,a=1,b=2,c=3)
foo(1, **{'a':1,'b':2,'c':3})

print("******************************************")
print("The usage of '*' and '**' :")
def foo(x, *args, **kwargs):
    print("x: {}".format(x))
    print("args: {}".format(args))
    print("kwargs: {}".format(kwargs))

foo(1,4,5,6, a=1,b=2,c=3)
foo(*(1,2,3))
foo(*(1,2,3), **{'a':1,'b':2,'c':3})