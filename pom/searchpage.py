from bases.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SearchPage(BaseElement):
    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__SEARCH_FIELD: str = "org.wikipedia:id/search_src_text"
        self.__SEARCH_RESULTS: str = "org.wikipedia:id/page_list_item_title"

    def __get_search_field(self) -> WebElement:
        return self._is_clickable('id', self.__SEARCH_FIELD, 'Search Field')

    def __get_search_results(self) -> List[WebElement]:
        return self._are_visible('id', self.__SEARCH_RESULTS, 'Search Results')

    def is_search_page_present(self) -> bool: return self.__get_search_field()

    def send_text_to_search_field(self, text: str): self.__get_search_field().send_keys(text)

    def is_search_result_correct_and_not_empty(self, text: str) -> bool:
        search_results = self.__get_search_results()
        if search_results:
            if all(text not in r.text.lower() for r in search_results):
                return False
        else:
            return False

        return True

    def select_result_and_click(self, index: int):
        search_results = self.__get_search_results()
        search_results[index].click()
