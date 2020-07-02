class Sample(object):
    def __init__(self):
        print("Sample init called")

    def __str__(self):
        return "Sample"


class A(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return Sample(*args, **kwargs)

    def __init__(self):
        print("A init called")

    def __str__(self):
        return "A"

class B(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super(B,cls).__new__(cls)

    def __init__(self):
        print("A init called")

    def __str__(self):
        return "B"

a = A()
print(f"object is {a}")
print("****************************")
b= B()
print(f"object is {b}")