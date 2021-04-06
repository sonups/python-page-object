from tests.coverage.markers import smoke
from demoauto.pages.careers import CareersPage
from demoauto.configuration.base_configuration import BaseConfiguration

@smoke
def test_join_us(base_config: BaseConfiguration, careers_page: CareersPage) -> None:
    assert careers_page.join_us().is_displayed()


# @smoke
# def test_one():
#     print("pass1")


# @smoke
# def test_header_page_platform(header_page: HeaderPage) -> None:
#     assert header_page.platform().is_displayed()
#
