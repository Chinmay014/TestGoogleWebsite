from selenium.webdriver.common.by import By
from pages.google_launch_page import LaunchPage
import time, re, pytest
from pages.google_search_results_page import SearchResultPage
from Utilities.utils import custLogger
from ddt import ddt,data,unpack
import unittest 

@pytest.mark.usefixtures("setup")
# @ddt
class TestGoogleSite:
    log = custLogger()
    log1 = log.customlogger()
    
    # @data(("Chocolate",))
    # @unpack
    def test_search_results(self):
        lp = LaunchPage(self.driver)
        search_result = lp.clickSearch("Chocolate")
        # print(f"Searching for {query}")
        # test 1: there should be non-zero results
        # find the corresponding element on search result page

        result_count = search_result.findResultsCount()
        # driver.close()
        self.log1.warning(f"found {result_count} results for Chocolate")
        assert result_count>0,"No results"

    # @data(("Chocolate",))
    # @unpack
    def test_search_quantity(self):
        # test 2: top suggested link contains the searched word atleast 5 times
        sp = SearchResultPage(self.driver)
        
        top_link = self.driver.find_element(By.XPATH,"//a[h3]")
        current_window = self.driver.current_window_handle

        sp.goToResultPage(top_link)

        page_word_count = sp.countWordOnPage("Chocolate")
        self.driver.quit()
        assert page_word_count>5

