import pytest
import sys

# Run pytest within the script
if __name__ == "__main__":
    # Skip writing pyc files on a readonly filesystem
    sys.dont_write_bytecode = True

    # Define the project and test cases directory
    project_name = "big_data_testing"
    test_cases_folder = "test_cases"

    # Construct the path to the test cases directory
    test_cases_path = "./test_cases"

    # Define the pytest flag with default value 'sanity'
    pytest_flag = "test_"

    # Check if a custom pytest flag is provided from the terminal
    # if len(sys.argv) > 1:
    #     pytest_flag = sys.argv[1]

    # Run the test cases with detailed logging and specific test expression
    retcode = pytest.main([
        "-v",
        "-p", "no:cacheprovider",
        "--tb=short",  # Short traceback format for easier reading
        "-k", pytest_flag,  # Run tests matching the specified expression
        test_cases_path  # Path to the test cases directory within the project
    ])

    # Fail the script execution if there are any test failures
    assert retcode == 0, "Some tests failed. Check the log above for details."