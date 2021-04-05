import pytest
from demoauto.browsers import WebBrowser
from demoauto.pages import Page
from demoauto.pages.home import HomePage
from demoauto.pages.register import RegisterPage
from demoauto.pages.header import HeaderPage
from demoauto.pages.demo import DemoPage
from demoauto.pages.careers import CareersPage


@pytest.fixture(scope="module")
def home_page(browser: WebBrowser) -> Page:
    return HomePage(browser)


@pytest.fixture(scope="module")
def register_page(browser: WebBrowser) -> Page:
    return RegisterPage(browser)

@pytest.fixture(scope="module")
def header_page(browser: WebBrowser) -> Page:
    return HeaderPage(browser)

@pytest.fixture(scope="module")
def demo_page(browser: WebBrowser) -> Page:
    return DemoPage(browser)

@pytest.fixture(scope="module")
def careers_page(browser: WebBrowser) -> Page:
    return CareersPage(browser)



