import random
import time
import datetime

"""
访问一个attribute的顺序如下：
1. 查找data descriptor, 并调用其__get__()方法
2. 查找对象的__dict__字典
3. 查找non data descriptor，并调用其__get__()方法
4. 查找类的__dict__字典
5. 查找父类的__dict__字典
"""
class DeepThought_1:
    def meaning_of_life(self):
        time.sleep(3)
        return 42

class LazyProperty_NonData:
    def __init__(self, function):
        self.func = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        instance.__dict__[self.name] = self.func(instance)
        return instance.__dict__[self.name]

class DeepThought_2:
    @LazyProperty_NonData
    def meaning_of_life(self):
        time.sleep(3)
        return 42

class LazyProperty_Data:
    def __init__(self, function):
        self.func = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        instance.__dict__[self.name] = self.func(instance)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        pass

class DeepThought_3:
    @LazyProperty_Data
    def meaning_of_life(self):
        time.sleep(3)
        return 42

thought_instance = DeepThought_1()
start = datetime.datetime.now()
print(thought_instance.meaning_of_life())
print(thought_instance.meaning_of_life())
print(thought_instance.meaning_of_life())
end = datetime.datetime.now()
print("DeepThought_1 cost ： {}".format(str((end-start).seconds)))

thought_instance = DeepThought_2()
start = datetime.datetime.now()
print(thought_instance.meaning_of_life)
print(thought_instance.meaning_of_life)
print(thought_instance.meaning_of_life)
end = datetime.datetime.now()
print("DeepThought_2 cost ： {}".format(str((end-start).seconds)))

thought_instance = DeepThought_3()
start = datetime.datetime.now()
print(thought_instance.meaning_of_life)
print(thought_instance.meaning_of_life)
print(thought_instance.meaning_of_life)
end = datetime.datetime.now()
print("DeepThought_2 cost ： {}".format(str((end-start).seconds)))