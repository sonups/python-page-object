from tests.coverage.markers import smoke
from demoauto.pages.demo import DemoPage
from demoauto.configuration.base_configuration import BaseConfiguration

@smoke
def test_request_demo_schedule_now(base_config: BaseConfiguration, demo_page: DemoPage) -> None:
    assert demo_page.schedule_now().is_displayed()

# @smoke
# def test_header_page_platform(header_page: HeaderPage) -> None:
#     assert header_page.platform().is_displayed()
#
