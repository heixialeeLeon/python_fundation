from abc import ABCMeta

class A(object):
    def method_a(self):
        print("method_a in class A")

class B(A):
    def __init__(self):
        pass

class C(object):
    def method_a(self):
        print("method_a in class C")

print("For the normal class inherit")
print("B is the sublcass of A: {}".format(issubclass(B, A)))
print("C is the sublcass of A: {}".format(issubclass(C, A)))

class AA(metaclass=ABCMeta):
    def method_aa(self):
        print("method_aa in class AA")

class BB(AA):
    def __init__(self):
        pass

class CC(metaclass=ABCMeta):
    def method_aa(self):
        print("method_aa in class CC")

print("")
print("For the abc class inherit without implement the __subclasshook__")
print("BB is the sublcass of AA: {}".format(issubclass(BB, AA)))
print("CC is the sublcass of AA: {}".format(issubclass(CC, AA)))

class AAA(metaclass=ABCMeta):
    def method_aa(self):
        print("method_aa in class AAA")

    @classmethod
    def __subclasshook__(cls, c):
        mro = c.__mro__
        for class_mro in mro:
            if "method_aa" in class_mro.__dict__:
                if class_mro.__dict__["method_aa"] is None:
                    raise NotImplemented
            break
        else:
            raise None
        return True

class BBB(AAA):
    def __init__(self):
        pass

class CCC(metaclass=ABCMeta):
    def method_aa(self):
        print("method_aa in class CC")

print("")
print("For the abc class inherit with implement the __subclasshook__")
print("BBB is the sublcass of AAA: {}".format(issubclass(BBB, AAA)))
print("CCC is the sublcass of AAA: {}".format(issubclass(CCC, AAA)))

print("AAA base class is {}".format(AAA.__base__))
print("BBB base class is {}".format(BBB.__base__))
print("CCC base class is {}".format(CCC.__base__))
