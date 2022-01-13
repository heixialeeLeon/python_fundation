import math
class Point:
    z = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

p = Point(1,1)

"""
类中的函数是在类的属性空间，不在实例对象的属性空间
"""
print("The class dict: {}".format(Point.__dict__.keys()))
print("The instance dict: {}".format(p.__dict__.keys()))
print("***************************************")

"""
类中的方法是function, 而实例中的方法只是一个bound method
"""
print("method in class: {}".format(Point.distance))
print("method in instance: {}".format(p.distance))
print("method type in class: {}".format(type(Point.distance)))
print("method type in instance: {}".format(type(p.distance)))
print("*********************************************")

"""
类中的方法其实是一种描述符
"""
print("__get__ in function: {}".format(hasattr(Point.distance, '__get__')))
print(type(Point.distance.__get__(p)))
# the address of the bound method
print("two way to get the address of the bound method: ")
print(id(Point.distance.__get__(p)))
print(id(p.distance))
# the address of the function
print("two way to get the address of the function: ")
print(id(Point.distance))
print(id(p.distance.__func__))
# the address of the instance
print("two way to get the address of the instance: ")
print(id(p))
print(id(p.distance.__self__))
print("**********************************************")

"""
method的另类调用方法
"""
bm = p.distance
print(bm())
print(bm.__func__(bm.__self__))