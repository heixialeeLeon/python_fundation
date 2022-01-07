import pytest

def foo():
    return 0

def foo_assert():
    raise TypeError()

def test_foo():
    assert foo() == 0

def test_foo_assert():
    with pytest.raises(TypeError):
        foo_assert()