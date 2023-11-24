from multiprocessing import Process, Manager

def f(d, l):
    d['a'] ="abc"
    d[1] = 99
    l.reverse()

def share_test():
    with Manager() as m:
        d = m.dict()
        l = m.list(range(10))
        print(f"type of d is {type(d)}")
        print(f"type of l is {type(l)}")
        p = Process(target=f,args=(d,l))
        p.start()
        p.join()
        print(d)
        print(l)

if __name__ == "__main__":
    share_test()