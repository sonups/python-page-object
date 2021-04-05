from typing import Callable
import pytest
from _pytest.fixtures import SubRequest
from demoauto.browsers import WebBrowser, WebBrowserError
from demoauto.browsers.chrome import Chrome
from demoauto.browsers.safari import Safari
from demoauto.browsers.firefox import FireFox
from demoauto.browsers.remote import WebBrowser, RemoteBrowser




def browser(request: SubRequest) -> Callable[[str], WebBrowser]:
    def browser_factory(name: str) -> WebBrowser:
        request.addfinalizer(lambda: target.driver().close())
        if name == "Chrome":
            target = Chrome()
            return target
        if name == "Safari":
            target = Safari()
            return target
        if name == "FireFox":
            target = FireFox()
            return target
        raise WebBrowserError(f"Browser {name} is not supported!")

    return browser_factory
