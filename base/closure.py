"""
The criteria that must be met to create closure in Python are summarized in the following points.
1. We must have a nested function (function inside a function).
2. The nested function must refer to a value defined in the enclosing function.
3. The enclosing function must return the nested function.
"""
def make_multiplier_of(n):

    def multiplier(x):
        return x*n

    return multiplier

def normal_function(n):
    return n*n

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(3))
print(times5(3))

print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)

"""
The normal function.__closure__ is None
The closure function.__closure__ is not None
"""
print("the difference of the function and closure")
print(normal_function.__closure__ is None)
print(times3.__closure__ is None)
print(times5.__closure__ is None)