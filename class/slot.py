from memory_profiler import profile

"""
Use the slot to limit will save the memory usage
"""

class Foobar(object):
    def __init__(self,x):
        self.x = x

class FoobarSlot(object):
    __slots__ = 'x'

    def __init__(self,x):
        self.x = x

@profile
def main1():
    f = [Foobar(42) for i in range(100000)]

@profile
def main2():
    f = [FoobarSlot(42) for i in range(100000)]

if __name__ == "__main__":
    main1()
    main2()