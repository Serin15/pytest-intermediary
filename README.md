Pytest Testing Suite

Overview

This project provides a comprehensive suite of unit tests using Pytest for various functionalities, including file handling, list operations, utility functions, and custom class testing. The tests cover multiple scenarios with fixtures, parameterized testing, and custom class testing.

Project Structure

.
├── tests
│   ├── test_fixture.py
│   ├── test_parametrize.py
│   └── test_utilities.py
├── main
│   └── main.py
└── README.md

Features Tested

1. Fixture-Based Testing

Creation of temporary files and directories

File existence verification

Content validation within files

Testing custom User class with methods like is_adult()

2. Parameterized Testing

is_even(number): Checks if a number is even with multiple inputs

divide(a, b): Divides two numbers, handling division by zero scenarios

is_palindrome(word): Checks if a word is a palindrome

is_valid_password(password): Validates password strength with diverse input cases

Installation

Clone the repository:

git clone https://github.com/your-username/pytest-testing-suite.git
cd pytest-testing-suite

Install dependencies:

pip install -r requirements.txt

Running Tests

To run all tests, use the following command:

pytest

To run specific tests:

pytest tests/test_fixture.py
pytest tests/test_parametrize.py

Example Output

==================== test session starts ====================
collected 20 items

tests/test_fixture.py ......                               [ 60% ]
tests/test_parametrize.py ......                           [100% ]

===================== 20 passed in 0.75s ====================

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License

This project is licensed under the MIT License.

Happy Testing!
