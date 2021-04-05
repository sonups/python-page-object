class HeaderLocators(object):
    """Represent home page web element locators."""

    our_customers: str = "//li[contains(@class,'hs-menu-item hs-menu-depth-1')]/a[text()='Our Customers ']"
    platform: str = "//li[contains(@class,'hs-menu-item hs-menu-depth-1')]/a[text()='Platform']"
    learn: str = "//li[contains(@class,'hs-menu-item hs-menu-depth-1')]/a[text()='Learn']"
    company: str = "//li[contains(@class,'hs-menu-item hs-menu-depth-1')]/a[text()='Company']"
    sign_in: str = "//li[contains(@class,'hs-menu-item hs-menu-depth-1')]/a[text()='Sign in']"
    request_a_demo: str = "//li[contains(@class,'hs-menu-item hs-menu-depth-1')]/a[text()='Request a Demo']"
