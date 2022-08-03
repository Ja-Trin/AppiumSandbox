from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.ui import WebDriverWait
from typing import List


class BaseElement:
    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.5)

    def __get_element_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'xpath': By.XPATH,
                    'id': By.ID,
                    'name': By.NAME,
                    'text': By.TAG_NAME}
        return locating[find_by]

    def _is_visible(self, find_by, locator: str, name: str = None) -> WebElement:
        return \
            self.__wait.until(exp_cond.visibility_of_element_located((self.__get_element_by(find_by), locator)), name)

    def _are_visible(self, find_by, locator: str, name: str = None) -> List[WebElement]:
        return \
            self.__wait.until(exp_cond.visibility_of_all_elements_located((self.__get_element_by(find_by), locator)), name)

    def _is_clickable(self, find_by, locator: str, name: str = None) -> WebElement:
        return \
            self.__wait.until(exp_cond.element_to_be_clickable((self.__get_element_by(find_by), locator)), name)
