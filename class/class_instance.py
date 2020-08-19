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