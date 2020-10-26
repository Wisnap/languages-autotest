import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None,
    #                 help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser_locale = request.config.getoption("language")
    options = Options()
    options.add_argument("--lang={}".format(browser_locale))
    browser = webdriver.Chrome(chrome_options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
