class A(object):
    def __init__(self):
        print(" --> enter A")
        super(A, self).__init__()
        print(" --> exit A")

class B(A):
    def __init__(self):
        print(" --> enter B")
        super(B, self).__init__()
        print(" --> exit B")

class C(A):
    def __init__(self):
        print(" --> enter C")
        super(C, self).__init__()
        print(" --> exit C")

class D(B, C):
    def __init__(self):
        print(" --> enter D")
        super(D, self).__init__()
        print(" --> exit D")

if __name__ == "__main__":
    c = C()
    print(C.__mro__)
    d = D()
    print(D.__mro__)