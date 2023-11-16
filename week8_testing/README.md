# Testing

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ianchen06/techin509?quickstart=1)

## Overview

There are two ways to write unit tests in Python

1. `unittest` package in the Python standard library. [table of assert methods](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)
1. `pytest`, a third-party library that has more features and less boilerplate code. [official doc](https://docs.pytest.org/)

When writing tests, make sure to keep the following in mind

1. **Test for Correctness**: The primary goal of unit tests is to verify that your code works as expected. Focus on writing tests that confirm the correctness of your code's behavior under various conditions, including edge cases.
1. **Prioritize Readability**: Tests serve as documentation for your code. They should be easy to read and understand, with clear intentions. This often means choosing descriptive names for test functions and making the test logic straightforward.
1. **Test One Thing at a Time**: A unit test should verify a single aspect of your code’s behavior. If a test fails, it should be clear what is broken. Avoid testing multiple behaviors in one test.

## Getting Started

1. Install `pytest`

    Run the following command in the terminal (For Windows users, make sure you select "Git Bash" for your terminal)
    ```bash
    pip install pytest
    ```

1. Navigate to the folders of each example in the terminal [instruction](../README.md)
1. Following the instruction in the README of each example to run the examples

## Examples

### Example 1 - Test a function - Square

Basic testing of a function

- [unittest](./example01_square_unittest/README.md)
- [pytest](./example01_square_pytest/README.md)

### Example 2 - Test a Class - Calculator

Testing a Class, with a test case that expects an Error. (divide by zero case)

- [unittest](./example02_calculator_unittest/README.md)
- [pytest](./example02_calculator_pytest/README.md)

### Example 3 - Test a Class with dependencies

Game class requires two dependencies during initialization, player1 and player2.
Because we don't need the behaviors of real players, instead of passing real players, we just use strings as players.

- [unittest](./example03_game_unittest/README.md)
- [pytest](./example03_game_pytest/README.md)

## Advanced Topocs (Optional)

### Example 10 - Use subTest/parameterized tests to run tests in a for loop for each test case

Increase code reuse in tests by running similar tests in a loop.
Just add more test cases in the test_cases list.

- [unittest](./example10_parameterized_tests_unittest/README.md)

### Example 11 - Mocking

What happens if you test some code with this code `input("please input a move?")`, the `input()` functions requires human input.

Sometimes we want to replace parts of the program so it is easier to test, (i.e. input() function)

- [unittest]()
- [pytest]()