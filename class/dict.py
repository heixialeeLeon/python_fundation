class Base:
    class_var_base = 0
    def __init__(self):
        self.instance_base_var = 0

base = Base()
print("base class and instance")
print("instance __dict__: ",base.__dict__)
print("class __dict__ :", Base.__dict__)
print("*****************************")
class Child(Base):
    class_var_child = 1
    def __init__(self):
        self.instance_child_var=1

print("child class and instance")
child = Child()
print("instance __dict__: ", child.__dict__)
print("class __dict__ :", Child.__dict__)
print("class dir: ",dir(Child))