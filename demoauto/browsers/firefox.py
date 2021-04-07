from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from demoauto.browsers import WebBrowser
from demoauto.driver.web_driver import WebDriverOf
from demoauto.driver.driver import Driver
import sys


class FireFox(WebBrowser):
    """Representation of a firefox web browser."""

    def __init__(self) -> None:
        self._firefox: WebDriver = webdriver.Firefox()

    def driver(self) -> Driver:
        return WebDriverOf(self._firefox)

    def name(self) -> str:
        return "Firefox"


class FirefoxLinux(WebBrowser):
    """Representation of a chrome web browser."""

    def __init__(self) -> None:
        print("sys-path" + sys.path[0])
        self._chrome: WebDriver = webdriver.Chrome(sys.path[0] + '/driver_executable/geckodriver')

    def driver(self) -> Driver:
        return WebDriverOf(self._chrome)

    def name(self) -> str:
        return "Chrome"

