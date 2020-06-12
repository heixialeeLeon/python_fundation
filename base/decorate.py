print("********************************************")
print("function decorator")

def common(func):
    def _deco(*args, **kwargs):
        print("args: ".format(args))
        return func(*args,**kwargs)
    return _deco

@common
def base(p):
    print(p)
base(1)

print("********************************************")
print("class decorator")

class common_class(object):
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("args:".format(args))
        return self.func(*args, **kwargs)

@common_class
def base_func(p):
    print(p)

base_func(1)

print("********************************************")
print("decorator function with parameter")

def common_para(param):
    print("get param: {}".format(param))

    def common_deco(func):
        print("get function: {}".format(func.__name__))

        def wrapper(*args, **kwargs):
            print("decro para: {}".format(param))
            print("args: ".format(args))
            return func(*args, **kwargs)
        return wrapper

    return common_deco

@common_para("abc")
def base_func(p):
    print(p)

base_func(1)

print("********************************************")
print("decorator class with parameter")

class common_class_arg(object):
    def __init__(self, arg):
        print("get param: {}".format(arg))
        self.arg = arg

    def __call__(self, func, *args, **kwargs):
        print("decorator args: {}".format(self.arg))
        def inner_func(*args, **kwargs):
            return func(*args, **kwargs)

        return inner_func

@common_class_arg("abc")
def base_func(p):
    print(p)

base_func(1)


