# Databricks Combined Notebook

import pytest
import sys

# Define a class for test cases
class TestMathOperations:
    def test_addition(self):
        assert 1 + 1 == 2, "Addition test failed"

    def test_subtraction(self):
        assert 5 - 3 == 2, "Subtraction test failed"