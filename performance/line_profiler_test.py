from line_profiler import LineProfiler
import random

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

def do_stuff(numbers):
    s = sum(numbers)
    l = [numbers[i]/43 for i in range(len(numbers))]
    m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

numbers = [random.randint(1,100) for i in range(1000)]

if __name__ == "__main__":
    lp = LineProfiler()
    lp_vs = lp(a)
    lp_vs()
    lp.print_stats()

    lp_stuf = lp(do_stuff)
    lp_stuf(numbers)
    lp.print_stats()