import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from appium import webdriver
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

    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Toledo, Spain")

    time.sleep(2)

    # search_results = browser.all((AppiumBy.CLASS_NAME, "android.widget.LinearLayout"))
    #
    # search_results.element_by(have.text("Toledo, Spain")).click()
    # browser.element((AppiumBy.CLASS_NAME, "android.widget.LinearLayout")).should(have.text("Toledo, Spain")).click()

    search_results = browser.all(
        (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Toledo, Spain')]"))

    # Найти элемент из результатов поиска, исключив окно поиска

    for result in search_results:
        if result != browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")):
            result.should(have.text('Toledo, Spain')).click()
            break
    time.sleep(3)
    # Проверка, что открылась правильная страница

    browser.element((AppiumBy.XPATH,
                                  "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/view_page_title']")).should(have.text('Toledo'))



    browser.quit()
