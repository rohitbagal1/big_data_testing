from py.xml import html
import pytest
from UtilityScripts.update_parameter_json import update_json_parameters

def pytest_html_report_title(report):
    report.title = "API Automation"


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group._addoption(
        "-S",
        dest="Server",
        default="reqres.in",
        help="this is our api server",
    )


def pytest_configure(config):
    config._metadata["Website URL"] = "https://reqres.in"
    if "-S" in config.invocation_params.args:
        server = config.getoption("-S")
        update_json_parameters("server", server)




def pytest_html_results_summary(prefix):
    prefix.extend([html.p("This demo framework is created by Rohit Bagal")])


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("Description"))
    cells.pop(2)
    cells.pop()  # to remove last column name



def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop(2)
    cells.pop()  # to remove last row values



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    try:
        report.description = str(item.function.__doc__) + " " + str((list(item.callspec.params.items())[0])[1])
    except:
        report.description = str(item.function.__doc__)
    print(report.description)
