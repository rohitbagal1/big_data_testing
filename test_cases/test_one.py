import pytest
from transformation.transformation_class import TransFormClass

class TestMathOperations:
    transformer = TransFormClass()  # Create an instance outside of any method

    def test_salary_one(self):
        status = self.transformer.execute_transformations()
        assert status == True, "Status is False hence test case failed"

    def test_salary_two(self):
        assert 5 - 3 == 2, "Subtraction test failed"