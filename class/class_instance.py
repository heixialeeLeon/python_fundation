from dataclasses import dataclass
class A:
    abc = 123
    def __init__(self):
        print("enter init ...")
        print(self.abc)
        self.abc = 0
        print("exit init ...")

a = A()
print(a.abc)
print(A.abc)

class B:
    abc = 123
    def __init__(self):
        pass

b = B()
print(b.__dict__)

class C:
    attr: int = 1
    percent: str = "c"

    def __init__(self):
        pass

c = C()
print(c.__dict__)
print(c.attr)

@dataclass
class D:
    attr: int = 1
    percent: str = "ok"

    def __init__(self):
        pass

"""
类变量在外部，可以通过intance.类变量 来访问，但是在其重新赋值后，两者就分开了
"""
print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
d = D()
print(d.__dict__)
print(d.attr)
print(id(d.attr))
print(D.attr)
print(id(D.attr))
d.attr = 10
print(d.attr)
print(D.attr)
print(d.percent)
print("instance percent :{}, class percent:{}".format(id(d.percent),id(D.percent)))
d.percent = "failed"
print("instance percent :{}, class percent:{}".format(id(d.percent),id(D.percent)))
print(d.percent)
print(D.percent)