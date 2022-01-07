class Foo(object):

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        print("call in __iter__")
        return self

    def __next__(self):
        print("call in __next__")
        if self.count == 0:
            raise StopIteration()
        self.count -= 1
        return self.count

foo = Foo(5)
for index, data in enumerate(foo):
    print("{}, {}".format(index, data))

print("*********************************")

foo = Foo(5)
for data in foo:
    print(data)