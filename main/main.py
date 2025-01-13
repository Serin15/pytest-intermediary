def is_even(number):
    return number % 2 == 0


def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(word):
    return word == word[::-1]


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True





