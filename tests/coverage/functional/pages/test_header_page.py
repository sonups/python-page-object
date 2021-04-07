from tests.coverage.markers import smoke
from demoauto.pages.header import HeaderPage
from demoauto.configuration.base_configuration import BaseConfiguration


@smoke
def test_header_page_our_customers(base_config: BaseConfiguration, header_page: HeaderPage) -> None:
    assert header_page.our_customers().is_displayed()
    assert header_page.platform().is_displayed()
    assert header_page.learn().is_displayed()
    assert header_page.company().is_displayed()
    assert header_page.sign_in().is_displayed()
    assert header_page.request_a_demo().is_displayed()
