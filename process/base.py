import multiprocessing
from multiprocessing import Process
import time

def test_func(x):
    return x*x

"""the different method to start a process"""

def fork_test():
    start = time.time()
    ctx = multiprocessing.get_context("fork")
    with ctx.Pool(100) as p:
        p.map(test_func, [x for x in range(1000)])
    end = time.time()
    print(f"cost {end - start:.5} s")

def spawn_test():
    start = time.time()
    ctx = multiprocessing.get_context("spawn")
    with ctx.Pool(100) as p:
        p.map(test_func, [x for x in range(1000)])
    end = time.time()
    print(f"cost {end - start:.5} s")

def forserver_test():
    start = time.time()
    ctx = multiprocessing.get_context("forkserver")
    with ctx.Pool(100) as p:
        p.map(test_func, [x for x in range(1000)])
    end = time.time()
    print(f"cost {end - start:.5} s")

def start_process_time():
    fork_test()
    spawn_test()
    forserver_test()

if __name__ == "__main__":
    start_process_time()
