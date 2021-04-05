import pytest
from demoauto.browsers.remote import WebBrowser, RemoteBrowser
from demoauto.browsers.chrome import WebBrowser, Chrome


@pytest.fixture(scope="session")
def browser() -> WebBrowser:
    browser: WebBrowser = RemoteBrowser()
    yield browser
    browser.driver().close()
