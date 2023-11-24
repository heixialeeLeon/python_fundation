class Student:
    __slots__ =("name","age")

if __name__ == "__main__":
    student = Student()
    print("init status: ")
    print("name: {}".format(hasattr(student,"name")))
    print("student: {}".format(hasattr(student,"age")))

    print("after assignment:")
    student.name="leon"
    student.age = "30"
    print("name: {}".format(hasattr(student,"name")))
    print("student: {}".format(hasattr(student,"age")))

    print("assignment out of the range of the slot")
    #student.country = "China"   # this will trigger error
    print("country: {}".format(hasattr(student,"country")))
    print(dir(student))