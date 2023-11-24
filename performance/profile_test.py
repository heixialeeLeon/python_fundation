import profile

def a():
    sum = 0
    for i in range(1,100000):
        sum += i
    return sum

def b():
    sum = 0
    for i in range(1,1000):
        sum += i
    return sum

if __name__ == "__main__":
    profile.run("a()")
    profile.run("b()")