class ConfigAttribute(object):
    """Makes an attribute forward to the config"""

    def __init__(self, name, get_converter=None):
        self.__name__ = name
        self.get_converter = get_converter

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        rv = obj.config[self.__name__]
        if self.get_converter is not None:
            rv = self.get_converter(rv)
        return rv

    def __set__(self, obj, value):
        obj.config[self.__name__] = value


class Foo(object):
    config= dict({
        "abc":1,
        "leon":2,
        "ABC":3
    })
    aa = ConfigAttribute("ABC")

    # def __getattribute__(self, item):
    #     print("in the __getattribute__")
    #     return super(Foo, self).__getattribute__(item)

foo = Foo()
x = foo.aa
print(x)
