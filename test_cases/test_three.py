import pytest
from transformation.transformation_two import TransFormClass

class TestMathOperations: 
    def test_employee_one(self):
        transformer = TransFormClass() 
        status = transformer.execute_transformations() 
        assert status == True, "Status is False hence test case failed"

    def test_employee_two(self):
        assert 5 - 3 == 2, "Subtraction test failed"