from contextlib import contextmanager

@contextmanager
def leon_assert():
    print("call before yield")
    yield
    print("call before yield")

with leon_assert():
    print("in the content")