from bases.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement


class ResultPage(BaseElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__RESULT_PAGE: str = "org.wikipedia:id/page_header_view"

    def __get_result_page(self) -> WebElement:
        return self._is_visible('id', self.__RESULT_PAGE, 'Result Page')

    def is_result_page_present(self) -> bool: return self.__get_result_page()
