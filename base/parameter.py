def test_param_0(param):
    print(type(param))

def test_param_1(*param):
    print(type(param))

def test_param_2(**param):
     print(type(param))

if __name__ == "__main__":
    str = 123
    test_param_0(str)
    test_param_1(str)
    test_param_2(param1=str, param2=str)