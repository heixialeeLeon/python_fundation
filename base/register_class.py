import inspect
from functools import partial

class Registry(object):
    def __init__(self, name):
        self._name = name
        self._module_dict = dict()

    @property
    def name(self):
        return self._name

    @property
    def module_dict(self):
        return self._module_dict

    def get(self, key):
        return self._module_dict.get(key, None)

    def _register_module(self, module_class):
        if not inspect.isclass(module_class):
            raise TypeError("not a class")
        module_name = module_class.__name__
        self._module_dict[module_name] = module_class

    def register_module(self, cls=None):
        if cls is None:
            return partial(self.register_module, force=force)
        self._register_module(cls)
        return cls

opt = Registry('test')

@opt.register_module
class A(object):
    def __init__(self):
        pass

@opt.register_module
class B(object):
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    print("abc")
    print("hello")
    AA = opt.get("A")()
    BB = opt.get("B")("BB")
    assert(True, isinstance(AA,A))
    assert(True, isinstance(BB,B))
    print("done")

