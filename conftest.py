import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome")
    parser.addoption('--language', action='store', default='ru')
    parser.addoption('--timeout', action='store', default=10,
                     help="Choose timeout time (seconds)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
        time.sleep(1)
        browser.maximize_window()

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(10)
        browser.maximize_window()

    else:
        print("Browser {} still is not implemented".format(browser_name))

    yield browser
    print("\nquit browser..")
    browser.quit()
