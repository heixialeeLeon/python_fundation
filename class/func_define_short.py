class Foo(object):
    def __init__(self):
        pass

    def abc(self):
        print("call in abc")

    efg = abc

print(Foo.__dict__)
print('abc' in Foo.__dict__)
print('efg' in Foo.__dict__)
foo = Foo()
foo.abc()
foo.efg()