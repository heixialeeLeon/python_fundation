class SomeClass:
    def __init__(self):
        pass

class SingleClass:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        pass

print("The Non Single mutli instance")
a = SomeClass()
b = SomeClass()
print("the a address is:{}, the b address is :{}".format(id(a),id(b)))
print("************************************")
print("The Singe Instance Mutli instance")
aa = SingleClass()
bb = SingleClass()
print("the aa address is:{}, the bb address is :{}".format(id(aa),id(bb)))