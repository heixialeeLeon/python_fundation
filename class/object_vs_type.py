class Meta(type):
    def __new__(cls, name, bases, dct):
        print("call in PluginMeta __new__")
        return super().__new__(cls, name, bases, dct)

class Object(object):
    def __new__(cls, *args, **kwargs):
        print("call in PlugObject __new__")
        return super().__new__(cls, *args, **kwargs)

class MetaSubClass(metaclass=Meta):
    def __init__(self):
        pass

class ObjectSubClass(Object):
    def __init__(self):
        pass

print("MetaSubClass create instance")
instance = MetaSubClass()
print("ObjectSubClass create instance")
instance = ObjectSubClass()
print("*******************************************")

print("The MetaSubClass MRO: {}".format(MetaSubClass.__mro__))
print("The ObjectSubClass MRO: {}".format(ObjectSubClass.__mro__))
print("*******************************************")

print("THe MetaSubClass Type MRO: {}".format(type(MetaSubClass).__mro__))
print("THe ObjectSubClass Type MRO: {}".format(type(ObjectSubClass).__mro__))