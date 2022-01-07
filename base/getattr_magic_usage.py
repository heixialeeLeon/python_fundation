class Foo(object):
    def __init__(self):
        pass

    def hello(self):
        print("call in Foo.hello")

    def goodbye(self):
        print("call in Foo.goodbye")

class Proxy(object):
    def __init__(self):
        self.foo = Foo

    def __getattr__(self, name):
        return getattr(self.foo, name)


proxy = Proxy()
proxy.hello(proxy)
proxy.goodbye(proxy)
print("done")