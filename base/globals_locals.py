abc = 1
print(globals())

class Student:
    def __init__(self):
        self.name = "aaa"

    def get_locals(self):
        print(locals())

    def get_globals(self):
        print(globals())

student = Student()
student.get_locals()
student.get_globals()