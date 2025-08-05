import pytest


def test_user_login():
    print('Hello!')

class TestUserLogin:
    def test_1(self):
        ...

    def test_2(self):
        ...


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5, '(2 + 2) != 5'


def test_zero_division(): 
    with pytest.raises(ZeroDivisionError): 
        1 / 0

def test_lists():
    assert [1, 2, 3] == [1, 2, 4]