"""
实现 __enter__ 和 __exit__接口
"""

class Context(object):
    def __init__(self):
        pass

    def __enter__(self):
        print("call in Context.__enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("call in Context.__exit__")

print("before the with")
with Context():
    print("in the with")
print("after the with")