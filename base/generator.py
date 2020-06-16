from collections.abc import Iterable

class my_iterator:
    def __init__(self, max=10):
        self.n = 0
        self.max = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        else:
            self.n+=1
            return self.n

def my_gen():
    n = 1
    print("first call")
    yield n

    n+=1
    print("second call")
    yield  n

    n+=1
    print("third call")
    yield n

it = my_iterator(3)
gen = my_gen()
print("it type: {}".format(type(it)))
print("it is iterable: {}".format(isinstance(it,Iterable)))
print(dir(it))
print("gen type: {}".format(type(gen)))
print("gen is iterable: {}".format(isinstance(gen,Iterable)))
print(dir(gen))

for item in gen:
    print(item)

"""
for the generator expression
"""
print("generator expression")
my_list = [1,2,3,4,5]
print(type([x**2 for x in my_list]))
print(type(x**2 for x in my_list))