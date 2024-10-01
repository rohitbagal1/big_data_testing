import pytest



def pytest_html_report_title(report):
    report.title = "UNIT TESTING REPORT"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["This testing report is focused on unit testing and utilizes a combination of Python, pytest, PySpark, and HTML as its building blocks. The framework is designed to assist data engineers in developing robust business logic and testing it effectively. By leveraging Python for scripting, pytest for test automation, PySpark for data processing, and HTML for generating informative reports, this framework provides a comprehensive solution for testing data pipelines and ensuring the reliability and correctness of business logic implementations."])
