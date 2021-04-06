import pytest

from demoauto.browsers.remote import WebBrowser, RemoteBrowser
from demoauto.browsers.chrome import WebBrowser, ChromeWindows, ChromeLinux
import demoauto.configuration.base_configuration as config

@pytest.fixture(scope="session")
def browser() -> WebBrowser:
    browser: WebBrowser
    if(config.global_data['os'] == 'windows'):
        browser = ChromeWindows()
    elif(config.global_data['os'] == 'linux'):
        browser = ChromeLinux()
    elif(config.global_data['os'] == 'remote'):
        browser = RemoteBrowser()
    yield browser
    browser.driver().close()


