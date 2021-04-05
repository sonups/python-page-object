class DemoLocators(object):
    """Represent Demo page web element locators."""

    schedule_now: str = "//div[contains(@class,'body-container-wrapper')]//descendant::h3[contains(text(),'Request a Demo')]/..//span[contains(@class,'align-center')]/a[contains(text(),'Schedule Now')]"