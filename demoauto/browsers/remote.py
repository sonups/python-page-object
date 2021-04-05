from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from demoauto.browsers import WebBrowser
from demoauto.driver.web_driver import WebDriverOf
from demoauto.driver.driver import Driver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class RemoteBrowser(WebBrowser):
    """Representation of a remote web browser."""

    def __init__(self, remote_url: str = "http://localhost:4444/wd/hub") -> None:
        hub_url = os.getenv('HUB_URL')
        hub_url = str(hub_url)
        if hub_url !='None':
            remote_url = hub_url
        self._remote: WebDriver = Remote(
            command_executor=remote_url, desired_capabilities=DesiredCapabilities.CHROME
        )

    def driver(self) -> Driver:
        return WebDriverOf(self._remote)

    def name(self) -> str:
        return "Remote"
