from tests.coverage.markers import smoke
from demoauto.pages.demo import DemoPage

@smoke
def test_request_demo_schedule_now(demo_page: DemoPage) -> None:
    assert demo_page.schedule_now().is_displayed()

# @smoke
# def test_header_page_platform(header_page: HeaderPage) -> None:
#     assert header_page.platform().is_displayed()
#
