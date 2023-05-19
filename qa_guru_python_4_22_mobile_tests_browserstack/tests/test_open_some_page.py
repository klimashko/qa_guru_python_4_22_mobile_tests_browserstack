import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser




def test_open_searching_page():
    # Options are only available since client version 2.3.0
    # If you use an older client then switch to desired_capabilities
    # instead: https://github.com/appium/python-client/pull/720
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-EK-MOBILE-DEMO",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": "evgenyklimashko_HCYP2F",
            "accessKey": "9khU39uhcNny1pmfajTg"
        }
    })

    # Initialize the remote Webdriver using BrowserStack remote URL
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    # Test case for the BrowserStack sample Android app.
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")


    elements = browser.elements((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
    for element in elements:
        if element.should(have.text("BrowserStack")) and element is not browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")):
            element.click()
            print(element)
            time.sleep(3)
            break


    browser.quit()
# element.should(have.no.id("org.wikipedia.alpha:id/search_src_text"))