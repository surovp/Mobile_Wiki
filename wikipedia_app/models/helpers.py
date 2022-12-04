from appium.webdriver.common.appiumby import AppiumBy


def accessibility_id(value: str):
    return (AppiumBy.ACCESSIBILITY_ID, value)


def selector_id(value: str):
    return (AppiumBy.ID, f"org.wikipedia.alpha:id/{value}")
