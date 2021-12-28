import typing as t
import time

def route(rule:str, **options: t.Any) -> t.Callable:

    def decorator(f:t.Callable)->t.Callable:
        print("call in decorator")
        print("str is {}".format(rule))
        print("option is {}".format(options))
        return f

    return decorator

@route("/abc", method=["post"])
def abc(a):
    print("call in abc and value is {}".format(a))


print(abc(11))
print("****************************")

def log_slow_call(func=None, threshold=1):
    def decorator(func):
        def proxy(*args, **kwargs):
            start_ts = time.time()
            result = func(*args, **kwargs)
            end_ts = time.time()

            seconds = end_ts - start_ts
            if seconds > threshold:
                print('slow call: {name} in {seconds}s'.format(
                name=func.__name__,
                seconds=seconds,
            ))

            return result

        return proxy

    if func is None:
        return decorator
    else:
        return decorator(func)

def log_slow_call_leon(threshold: int):
    def decorator(f:t.Callable)->t.Callable:
        def proxy_leon(*args, **kwargs):
            start_ts = time.time()
            result = f(*args, **kwargs)
            end_ts = time.time()

            seconds = end_ts - start_ts
            if seconds > threshold:
                print('slow call: {name} in {seconds}s, threshold:{threshold}'.format(
                    name=f.__name__,
                    seconds=seconds,
                    threshold = threshold
                ))
            return result
        return proxy_leon
    return decorator

@log_slow_call(threshold=2)
def sleep_seconds_a(seconds):
    time.sleep(seconds)

print(sleep_seconds_a.__name__)
sleep_seconds_a(3)
print("done")

@log_slow_call_leon(threshold=2)
def sleep_seconds_b(seconds):
    time.sleep(seconds)

print(sleep_seconds_b.__name__)
sleep_seconds_b(3)
print("done")