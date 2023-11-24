"""
1. An object can be iterated over with "for" if it implements
   __iter__() or __getitem__().

2. An object can function as an iterator if it implements next().
"""

class Foo_getitem(object):
    def __init__(self, count):
        self.count = count

    def __getitem__(self, index):
        print("call in __getitem__ {}".format(index))
        if index > self.count:
            raise IndexError()
        return index


class Foo_iter(object):
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        print("call in __iter__" )
        return self

    def __next__(self):
        print("call in __next__ {}".format(self.count))
        self.count -= 1
        if self.count == 0:
            raise StopIteration()


print("The __getitem__ implement in the for statement")
foo_getitem = Foo_getitem(5)
for i in foo_getitem:
    print(i)

print("*****************************")
print("The __iter__  and __next__ implement in the for statement")

foo_iter = Foo_iter(5)
for i in foo_iter:
    print(i)

print("******************************")
print("The type difference: ")
from typing import Iterable, Iterator
print("foo_getitem is Iterable: {}".format(isinstance(foo_getitem, Iterable)))
print("foo_getitem is Iterator: {}".format(isinstance(foo_getitem, Iterator)))
print("foo_iter is Iterable: {}".format(isinstance(foo_iter, Iterable)))
print("foo_iter is Iterator: {}".format(isinstance(foo_iter, Iterator)))
