class People(object):
    people_name = "leon"
    def __init__(self):
        self.name = "haha"

    @classmethod
    def get_name(cls):
        print("call in class method:")
        return cls.people_name

    @staticmethod
    def get_name_static():
        print("call in static method")
        return People.people_name

if __name__ =="__main__":
    print("Call the class and static method by the class name")
    print(People.get_name())
    print(People.get_name_static())
    print("Call the class and static method by the instance")
    p = People()
    print(p.get_name())
    print(p.get_name_static())
    print(p.__getattribute__("name"))

    print(dir(p))
    p.abc = 1
    print(dir(p))