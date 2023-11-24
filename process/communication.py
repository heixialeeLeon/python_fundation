import multiprocessing
from multiprocessing import Process,Queue, Pipe
import time

def queue_put(q, param):
    q.put(param)

def queue_test():
    q = Queue()
    p1 = Process(target=queue_put, args=(q,(1,"process"),))
    p2 = Process(target=queue_put, args=(q,(2,"process"),))
    p1.start()
    p2.start()
    time.sleep(1)
    while not q.empty() :
        print(q.get())
    p1.join()
    p2.join()

def pipe_send(conn):
    conn.send("hello")

def pipe_test():
    p_conn, c_conn = Pipe()
    p = Process(target=pipe_send, args=(c_conn,))
    p.start()
    print(p_conn.recv())
    p.join()

if __name__ == "__main__":
    queue_test()
    pipe_test()