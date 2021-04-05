from tests.coverage.markers import smoke
from demoauto.pages.careers import CareersPage
print("pass1")
@smoke
def test_join_us(careers_page: CareersPage) -> None:
    assert careers_page.join_us().is_displayed()


# @smoke
# def test_one():
#     print("pass1")


# @smoke
# def test_header_page_platform(header_page: HeaderPage) -> None:
#     assert header_page.platform().is_displayed()
#
