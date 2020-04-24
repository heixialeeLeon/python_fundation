class Base:
    def base1(self):
        pass
    def base2(self):
        pass

class MyClass:
    def method(self):
        return 1

print(dir(MyClass))

kclass = type('MyClass2',(Base,),{'method':123})
aa = kclass()
print(kclass.__dict__)
print(dir(aa))

print(dir(type))