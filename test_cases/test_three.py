import pytest
from transformation.transformation_two import TransFormClass
class TestMathOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.transformer = TransFormClass()
    
    def test_employee_one(self):
        status = self.transformer.execute_transformations()
        assert status==True, "Status is False hence test case failed"

    def test_employee_two(self):
        assert 5 - 3 == 2, "Subtraction test failed"



