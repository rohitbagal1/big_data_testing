import pytest
from datetime import datetime

# Hook for making reports
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Customize the HTML report table header
def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')
    cells.insert(1, '<th class="sortable time" col="time">Time</th>')
    cells.pop()

# Customize the HTML report table row
def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{getattr(report, "description", "")}</td>')
    cells.insert(1, f'<td class="col-time">{getattr(report, "duration", 0)}</td>')
    cells.pop()

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
