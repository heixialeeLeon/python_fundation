def common(func):
    def _deco(*args, **kwargs):
        print("args: ".format(args))
        return func(*args,**kwargs)
    return _deco

@common
def base(p):
    print(p)

print("function as the decorator")
print(base)
base(1)
print("************************")

class common_class(object):
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("args:".format(args))
        return self.func(*args, **kwargs)

@common_class
def base_func(p):
    print(p)

print("class as the decorator")
print(base_func)
base_func(1)

print("********************************************")
print("decorator with parameter")

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
