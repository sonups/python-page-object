import sys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from demoauto.browsers import WebBrowser
from demoauto.driver.web_driver import WebDriverOf
from demoauto.driver.driver import Driver


class ChromeWindows(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        self._chrome: WebDriver = webdriver.Chrome(sys.path[0] + '\\driver_executable\\chromedriver.exe')

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return "Chrome"


class ChromeLinux(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        print("sys-path" + sys.path[0])
        self._chrome: WebDriver = webdriver.Chrome(sys.path[0] + '/driver_executable/chromedriver')

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return "Chrome"
