import pytest
from main.main import is_even
from main.main import divide
from main.main import is_palindrome
from main.main import is_valid_password


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False)
])
def test_is_even(number, expected):
    assert is_even(number) == expected


@pytest.mark.parametrize("a,b, expected", [
    (10, 2, 5),
    (15, 5, 3),
    (20, 10, 2),
])
def test_divide_valid(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a,b", [
    (10, 0),
    (-1, 0)
])
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(a, b)


@pytest.mark.parametrize("word, expected", [
    ("racecar", True),
    ("python", False)
])
def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected


@pytest.mark.parametrize("password, expected", [
    ("Password1", True),
    ("password1", False),
    ("Password", False),
    ("Pass1", False),
    ("P4ssword", True),
])
def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected
