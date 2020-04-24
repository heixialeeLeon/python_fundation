from inspect import isfunction

class Student:
    def __init__(self):
        self.name = "leon"
        self.age = 0

    def study(self):
        #print("call in the study method")
        return

    @property
    def school(self):
        #print("call in the school method")
        return "SouthEast"

student =Student()
print(dir(student))

print("attribute test **********************")
print("name: {}".format(hasattr(student,"name")))
print("age: {}".format(hasattr(student,"age")))
print("study: {}".format(hasattr(student,"study")))
print("school: {}".format(hasattr(student,"school")))
print("*************************************")

print("the attribute displacement, the method is also be the attribute and can be displacement")
print("study type: {}".format(type(student.study)))
student.study()
student.study = "abc"
print("study type: {}".format(type(student.study)))
#student.study()  # this will cause the error
print("************************************")

print("the @property will change the func as a readonly attribute")
print(student.school)
#student.school = "abc"  # this will trigger error
print("************************************")

print("the type for variable, method and property")
student = Student()
print("name type: {}".format(type(student.name)))
print("study type: {}".format(type(student.study)))
print("school type: {}".format(type(student.school)))

