import os
import pytest
from appium import webdriver
import sys

sys.path.append("../src/")

import src.config as c
import src.test_data as td


@pytest.fixture()
def get_webdriver():
    caps = {
        "platformName": c.platformName,
        "platformVersion": c.platformVersion,
        "deviceName": c.deviceName,
        "app": f"{os.getcwd()}/app_binaries/{td.apk_name}",
        "noReset": True,
        "fullReset": False
    }

    driver = webdriver.Remote(c.url, desired_capabilities=caps)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
