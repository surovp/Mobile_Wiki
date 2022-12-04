import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def app_config():

    USER_NAME = os.getenv('USER_NAME')
    KEY = os.getenv('KEY')
    APP = os.getenv('APP')

    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": APP,

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Diploma project for Mobile automation",
            "buildName": "browserstack-build-DEMO With helpers",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": USER_NAME,
            "accessKey": KEY
    }
})
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
