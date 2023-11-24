"""
The usage difference between get and setdefault
"""
d = dict({"a":0, "b":1})
print(d.get("c",3))
print(d)
print(d.setdefault("c",3))
print(d)