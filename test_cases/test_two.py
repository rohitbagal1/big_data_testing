import pytest
from transformation.transformation_one import TransFormClass

class TestMathOperations: 
    transformer = TransFormClass()
    def test_product_one(self): 
        status = self.transformer.execute_transformations() 
        assert status == True, "Status is False hence test case failed"

    def test_product_two(self):
        assert 5 - 3 == 2, "Subtraction test failed"