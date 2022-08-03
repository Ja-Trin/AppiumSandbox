from bases.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement


class MainPage(BaseElement):
    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__MAIN_PAGE_LOGO: str = "org.wikipedia:id/main_toolbar_wordmark"
        self.__MAIN_SEARCH: str = "org.wikipedia:id/search_container"

    def __get_main_logo(self) -> WebElement: return self._is_visible('id', self.__MAIN_PAGE_LOGO, 'Main page Logo')

    def __get_search_combobox(self) -> WebElement: return self._is_clickable('id', self.__MAIN_SEARCH, 'Search Combobox')

    def is_main_page_present(self) -> bool: return self.__get_main_logo()

    def click_search_combobox(self): self.__get_search_combobox().click()
