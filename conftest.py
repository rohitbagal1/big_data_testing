import pytest
from pytest_html import html
from datetime import datetime

# Hook for making reports
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    try:
        report.description = str(item.function.__doc__) + " " + str((list(item.callspec.params.items())[0])[1])
    except:
        report.description = str(item.function.__doc__)
    print(report.description)


# Customize the HTML report table row
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("Description"))
    cells.pop(2)
    cells.pop()  # to remove last column name

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop(2)
    cells.pop()  # to remove last row values


# Set the report title
def pytest_html_report_title(report):
    report.title = "Pytest Automation Report"

# Add metadata to the report
def pytest_configure(config):
    config.option.metadata = {}
    config.option.metadata['Project Name'] = 'Your Project Name'
    config.option.metadata['Tester'] = 'Your Name'

def pytest_html_results_summary(prefix):
    prefix.extend([html.p("This demo framework is created by Rohit Bagal")])

# Add a summary message to the report
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"<p>Generated at: {datetime.now()}</p>"])

# Remove screenshots from the HTML report
def pytest_html_results_table_html(report, data):
    if 'extra' in data:
        del data['extra']
