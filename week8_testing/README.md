# Testing

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ianchen06/techin509?quickstart=1)

## Overview

There are two ways to write unit tests in Python

1. `unittest` package in the Python standard library
1. `pytest`, a third-party library that has more features and less boilerplate code

## Getting Started

1. Install `pytest`

    Run the following command in the terminal (For Windows users, make sure you select "Git Bash" for your terminal)
    ```bash
    pip install pytest
    ```

1. Navigate to the folders of each example in the terminal
1. Following the instruction in the README of each example to run the examples

## Examples

### Example 1 - Test a function - Square

Basic testing of a function

- [unittest](./example1_square_unittest/README.md)
- [pytest](./example1_square_pytest/README.md)

### Example 2 - Test a Class - Calculator

Testing a Class, with a test case that expects an Error. (divide by zero case)

- [unittest](./example2_calculator_unittest/README.md)
- [pytest](./example2_calculator_pytest/README.md)

### Example 3 - Test a Class with dependencies

Game class requires two dependencies during initialization, player1 and player2.
Because we don't need the behaviors of real players, instead of passing real players, we just use strings as players.

- [unittest](./example3_game_unittest/README.md)
- [pytest](./example3_game_pytest/README.md)

### Example 9 - Use subTest/parameterized tests to run tests in a for loop for each test case

Increase code reuse in tests by running similar tests in a loop.
Just add more test cases in the test_cases list.

- 