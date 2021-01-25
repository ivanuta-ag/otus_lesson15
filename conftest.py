import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
import logging

logging.basicConfig(level=logging.INFO, filename="h:/repo/lesson15_homework/logs/selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info("===> Test {} started".format(test_name))

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)

    elif browser == "ie":
        driver = webdriver.Ie()

    elif browser == "remote_firefox":
        capabilities = {
            "acceptInsecureCerts": True,
            "browserName": "firefox",
            "version": "61.0",
            "enableVNC": True,
            "enableVideo": False,
        }
        driver = webdriver.Remote(command_executor="http://10.5.29.233:4444/wd/hub", desired_capabilities=capabilities)

    elif browser == "remote_chrome":
        capabilities = {
            "acceptInsecureCerts": True,
            "browserName": "chrome",
            "version": "73.0",
            "enableVNC": True,
            "enableVideo": False,
        }
        driver = webdriver.Remote(command_executor="http://10.5.29.233:4444/wd/hub", desired_capabilities=capabilities)


    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or ie")

    logger.info("Browser {} started with {}".format(browser, driver.desired_capabilities))
    driver.maximize_window()

    def fin():
        driver.close()
        logger.info("Browser {} closed".format(browser))
        logger.info("===> Test {} finished".format(test_name))

    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture()
def main_page(browser):
    page = MainPage(browser, base_url=browser.current_url + "/index.php?route=account/login")
    page.go_to()
    return page
