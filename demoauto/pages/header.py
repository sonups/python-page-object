from demoauto.browsers import WebBrowser
from demoauto.driver.driver import Driver
from demoauto.map.elements import Element
from demoauto.map.handlers import HandlerBy, WebHandlerBy
from demoauto.locators.header import HeaderLocators as HP_Locators
from demoauto.pages import Page
from demoauto.pages.base import BasePage
from demoauto.map.urls import DemoPageUrl, Url


class HeaderPage(Page):
    """Represent Header page."""

    def __init__(self, browser: WebBrowser) -> None:
        self._by: HandlerBy = WebHandlerBy()
        self._hp_locators: HP_Locators = HP_Locators()
        self._page: Page = BasePage(browser, DemoPageUrl())

    def driver(self) -> Driver:
        return self._page.driver()

    def open(self, url: Url = None) -> None:
        self._page.open(url)

    def close(self) -> None:
        self._page.close()

    def our_customers(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.our_customers)

    def platform(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.platform)

    def learn(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.learn)

    def company(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.company)

    def sign_in(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.sign_in)

    def request_a_demo(self) -> Element:
        return self.driver().find_element(self._by.xpath(), self._hp_locators.request_a_demo)
