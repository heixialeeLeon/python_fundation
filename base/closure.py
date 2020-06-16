def make_multiplier_of(n):

    def multiplier(x):
        return x*n

    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(3))
print(times5(3))

print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)