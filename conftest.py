import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture()
# this will excuate at in the begning

def setup(browser):
    if browser == 'chrome':
        chromedriver_path = ChromeDriverManager().install()
        print(f"Chromedriver path: {chromedriver_path}")
        chrome_service = ChromeService(chromedriver_path)
        driver = webdriver.Chrome(service=chrome_service)
    elif browser == 'edge':
        edgedriver_path = EdgeChromiumDriverManager().install()
        print(f"Edge driver path: {edgedriver_path}")
        edge_service = EdgeService(edgedriver_path)
        driver = webdriver.Edge(service=edge_service)
    elif browser == 'firefox':
        geckodriver_path = GeckoDriverManager().install()
        print(f"Geckodriver path: {geckodriver_path}")
        firefox_service = FirefoxService(geckodriver_path)
        driver = webdriver.Firefox(service=firefox_service)
    #
    # print("lanching")
    return driver
    # yield
    # print("quting")

    # /yeild will excuate at the end of the project


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')
# its is hook to adding enivroment to html report

def pytest_configure(config):
    # Ensure the metadata attribute exists
    if not hasattr(config, '_metadata'):
        config._metadata = {}

    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Login Page'
    config._metadata['Tester Name'] = 'Lohith'
    print("Metadata configured jguyguguy:", config._metadata)
#
# # Optionally, you can modify the environment info
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


