class Property:
    def __init__(self, fget=None, fset=None, fdel=None):
        print(">>> enter Property.__init__")
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        print("<<< exit Property.__init__")

    def __get__(self, instance, cls):
        print(">>> enter Property.__get__")
        if self.fget is not None:
            return self.fget(instance)

    def __set__(self, instance, value):
        print(">>> enter Property.__set__")
        if self.fset is not None:
            self.fset(instance, value)

    def __delete__(self, instance):
        print(">>> enter Property.__delete__")
        if self.fdel is not None:
            self.fdel(instance)

    def getter(self, fn):
        print(">>> enter Property.getter")
        self.fget = fn

    def setter(self, fn):
        print(">>> enter Property.setter")
        self.fset = fn

    def deler(self, fn):
        print(">>> enter Property.deler")
        self.fdel = fn

class Spam:
    def __new__(cls, *args, **kwargs):
        print(">>> enter Spam.__new__")
        return super(Spam, cls).__new__(cls)

    def __init__(self, val):
        print(">>> enter Spam.__init__")
        self.__val = val

    @Property
    def val(self):
        print(">>> enter Spam.val")
        return self.__val

    @val.setter
    def set_val(self, value):
        print(">>> enter Spam.set_val")
        self.__val = value

class Spam_NoSuager(object):

    def __init__(self, val):
        print(">>> enter Spam_NoSuager.__init__")
        self.__val = val

    def _val(self):
        print(">>> enter Spam_NoSuager.val")
        return self.__val

    def _set_val(self, value):
        print(">>> enter Spam_NoSuager.set_val")
        self.__val = value

    val = Property(_val, _set_val)

s = Spam(4)
print("*********************")
print(s.val)
s.val = 99
print(s.val)

print("*********no sugar********************")
ss = Spam_NoSuager(4)
print(ss.val)
ss.val = 100
print(ss.val)

print("****************************************************")
print("anthoer simple way to use the property")

class Foo(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def _callback_proptrey(name):
        def fget(self):
            print("call in fget")
            return getattr(self, name)

        def fset(self, value):
            print("call in fset")
            setattr(self, name, value)

        return property(fget, fset)

    a = _callback_proptrey("_a")
    b = _callback_proptrey("_b")
    c = _callback_proptrey("_c")
    del _callback_proptrey

foo = Foo(1,2,3)
print(foo.a)
foo.b =10
print(foo.b)