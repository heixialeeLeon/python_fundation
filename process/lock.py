from multiprocessing import Process, Lock
import time

def func_lock(l, i):
    l.acquire()
    try:
        print(f"func: {i}")
        time.sleep(1)
    finally:
        l.release()

def func_no_lock(l, i):
    print(f"func: {i}")
    time.sleep(1)

def lock_test():
    print("no lock test ****")
    for num in range(10):
        Process(target=func_no_lock, args=(func_no_lock, num)).start()

    lock = Lock()
    print("with lock test ****")
    for num in range(10):
        Process(target=func_lock, args=(lock,num)).start()

if __name__ == "__main__":
    lock_test()