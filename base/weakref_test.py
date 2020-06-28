import weakref
import sys

class RefObject:
    def __del__(self):
        print("del excute")

def weakref_test():
    print("weakref_test ******************************")
    obj = RefObject()
    print("init reference count: {}".format(sys.getrefcount(obj)))
    A = obj
    print("reference count: {}".format(sys.getrefcount(obj)))
    B = A
    print("reference count: {}".format(sys.getrefcount(obj)))
    C = weakref.ref(obj)
    print("reference count: {}".format(sys.getrefcount(obj)))

def weakref_usage_test():
    print("weakref_usage_test **************************")
    obj = RefObject()
    r = weakref.ref(obj)
    print("r: {}".format(r))
    print("r(): {}".format(r()))

def weakref_final_test():
    print("weakref_final_test **************************")

    def on_finalize(*args):
        print(f"on_finalize: {args}")

    obj = RefObject()
    weakref.finalize(obj, on_finalize, "callback parameters")
    del obj

def weakref_finial_self_test():
    print("weakref_finial_self_test **************************")

    def on_finalize(*args):
        print(f"on_finalize: {args}")

    obj = RefObject()
    obj_id = id(obj)
    f = weakref.finalize(obj, on_finalize, obj)
    f.atexit = False
    del obj

    import gc
    for o in gc.get_objects():
        if id(o) == obj_id:
            print("find uncolletected object in gc")

def weakref_proxy_test():
    print("weakref_proxy_test **************************")
    obj = RefObject()
    r = weakref.ref(obj)
    p = weakref.proxy(obj)
    print("r: {}".format(r))
    print("r(): {}".format(r()))
    print("p: {}".format(p))

def custom_weakref_test():
    print("custom_weakref_test **************************")
    class A:
        __slots__ =('name','age')
        def __init__(self,name, age):
            self.name = name
            self.age = age

        # def __str__(self):
        #     return f"name is {self.name}, age is {self.age}"

    class B:
        __slots__ =('name','age','__weakref__')
        def __init__(self,name, age):
            self.name = name
            self.age = age

        # def __str__(self):
        #     return f"name is {self.name}, age is {self.age}"

    a = A("abc",10)
    try:
        r = weakref.proxy(a)
        print(f"{dir(r)}")
    except TypeError as e:
        print(e)

    b = B("abc",10)
    try:
        r = weakref.proxy(b)
        print(f"{r}")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    weakref_test()
    weakref_usage_test()
    weakref_final_test()
    weakref_finial_self_test()
    weakref_proxy_test()
    custom_weakref_test()