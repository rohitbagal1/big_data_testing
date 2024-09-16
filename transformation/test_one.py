# Databricks Combined Notebook




import pytest
from test_data import data
from transformation.transformation_class import TransFormClass
class TestMathOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.transformer = TransFormClass()
    
    def test_addition(self):
        
        df = self.transformer.execute_transformations(data.columns_to_add, data.columns_to_drop, data.column_to_capitalize)
        assert df.collect()!=df.collect(),"having hava error"

    def test_subtraction(self):
        assert 5 - 3 == 2, "Subtraction test failed"


# Run pytest within the notebook
# if __name__ == "__main__":

#     # Skip writing pyc files on a readonly filesystem
#     sys.dont_write_bytecode = True

#     # Run the test cases with detailed logging
#     retcode = pytest.main([
#         "-v",
#         "-p", "no:cacheprovider",
#         "--tb=short"  # Short traceback format for easier reading
#     ])

#     # Fail the cell execution if there are any test failures
#     assert retcode == 0, "Some tests failed. Check the log above for details."
