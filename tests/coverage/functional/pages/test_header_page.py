from tests.coverage.markers import smoke
from demoauto.pages.header import HeaderPage
import pytest
from demoauto.browsers.remote import WebBrowser, RemoteBrowser
from demoauto.browsers.chrome import WebBrowser, Chrome

# @pytest.fixture()
# def browser() -> WebBrowser:
#     browser: WebBrowser = RemoteBrowser()
#     yield browser
#     browser.driver().close()

@smoke
def test_header_page_our_customers(header_page: HeaderPage) -> None:
    assert header_page.our_customers().is_displayed()
    assert header_page.platform().is_displayed()
    assert header_page.learn().is_displayed()
    assert header_page.company().is_displayed()
    assert header_page.sign_in().is_displayed()
    assert header_page.request_a_demo().is_displayed()
