import pytest
from datetime import datetime
from pytest_html import extras

# Hook for making reports
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(report.duration, class_='col-time'))
    cells.pop()

def pytest_html_report_title(report):
    report.title = "Pytest Automation Report"

def pytest_configure(config):
    # Ensure pytest-html plugin is available
    if config.pluginmanager.hasplugin("html"):
        config._metadata = config._metadata or {}
        config._metadata['Project Name'] = 'Your Project Name'
        config._metadata['Tester'] = 'Your Name'
    else:
        print("pytest-html plugin is not available. Metadata will not be added.")

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Generated at: {0}".format(datetime.now()))])

def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
