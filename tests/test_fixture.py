import pytest


@pytest.fixture()
def temporary_file(tmpdir):
    file = tmpdir.join("sample.txt")
    file.write("This is a temporary file for testing.")
    return file


def test_read_file(temporary_file):
    with open(str(temporary_file), 'r') as f:
        content = f.read()
    assert content == "This is a temporary file for testing."


# Fixture for creating a temporary directory with files
@pytest.fixture()
def temporary_directory_with_files(tmpdir):
    file1 = tmpdir.join("sample1.txt")
    file1.write("First text")
    file2 = tmpdir.join("sample2.txt")
    file2.write("Second text")
    # Return the temporary directory and file list
    return tmpdir, [file1, file2]


# File existence check test

def test_file_exist(temporary_directory_with_files):
    tmpdir, files = temporary_directory_with_files

    for file in files:
        assert file.exists(), f"{file} does not exist!"


# Test for checking file content

def test_for_checking_file(temporary_directory_with_files):
    tmpdir, files = temporary_directory_with_files
    expected_contents = ["First text", "Second text"]

    for file, expected_contents in zip(files, expected_contents):
        assert file.read() == expected_contents, f"Content of {file} is incorrect!"


# Creates a fixture that generates a list of data (for example, a list of numbers, strings, or complex objects).

# Test that checks list length
# Test that checks the items in the list
# Test that checks if all items are greater than 0
# Test for list operations (descending sort)
# Test if an element is present in the list


@pytest.fixture()
def number_list():
    return [1, 2, 3, 4, 5]


def test_number_list(number_list):
    assert len(number_list) == 5


def test_list_element(number_list):
    assert number_list == [1, 2, 3, 4, 5]


def test_all_elements_positive(number_list):
    assert all(x > 0 for x in number_list)


def test_list_sorting(number_list):
    sorted_list = sorted(number_list, reverse=True)
    assert sorted_list == [5, 4, 3, 2, 1]


def test_element_in_list(number_list):
    assert 3 in number_list


# Testing a Fixture that Creates a Complex Object

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18


@pytest.fixture()
def user_fixture():
    return User(name="Serin", age=24)


def test_user_initialization(user_fixture):
    user = user_fixture
    assert user.name == "Serin"
    assert user.age == 24


def test_user_is_adult(user_fixture):
    user = user_fixture
    assert user.is_adult() is True
