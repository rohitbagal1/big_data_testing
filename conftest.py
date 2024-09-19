import pytest
from datetime import datetime

# Hook for making reports
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')
    cells.insert(1, '<th class="sortable time" col="time">Time</th>')
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{getattr(report, "description", "")}</td>')
    cells.insert(1, f'<td class="col-time">{getattr(report, "duration", 0)}</td>')
    cells.pop()

def pytest_html_report_title(report):
    report.title = "Pytest Automation Report"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if config.pluginmanager.hasplugin("html"):
        config._metadata = getattr(config, '_metadata', {})
        config._metadata['Project Name'] = 'Your Project Name'
        config._metadata['Tester'] = 'Your Name'
    else:
        print("pytest-html plugin is not available. Metadata will not be added.")

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"<p>Generated at: {datetime.now()}</p>"])

def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
