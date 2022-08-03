import pytest
from src import test_data as td
from pom.mainpage import MainPage
from pom.searchpage import SearchPage
from pom.resultpage import ResultPage


@pytest.mark.usefixtures('setup')
class TestSandbox:

    def test_sandbox(self):
        mainpage = MainPage(self.driver)
        assert mainpage.is_main_page_present()
        mainpage.click_search_combobox()

        searchpage = SearchPage(self.driver)
        assert searchpage.is_search_page_present()
        searchpage.send_text_to_search_field(td.look_up_text.lower())
        assert searchpage.is_search_result_correct_and_not_empty(td.look_up_text.lower())
        searchpage.select_result_and_click(td.search_index)

        resultpage = ResultPage(self.driver)
        assert resultpage.is_result_page_present()



