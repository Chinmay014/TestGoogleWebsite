from selenium.webdriver.common.by import By
from pages.google_launch_page import LaunchPage
import time, re, pytest
from pages.google_search_results_page import SearchResultPage
from Utilities.utils import custLogger
from ddt import ddt,data,unpack, file_data
import unittest 

@pytest.mark.usefixtures("setup")
@ddt
class TestGoogleSite(unittest.TestCase):
    log = custLogger()
    log1 = log.customlogger()
    

    @file_data("../TestData/testdata.json")
    def test_search_results(self,search_query):
        lp = LaunchPage(self.driver)
        search_result = lp.clickSearch(search_query)
        # print(f"Searching for {query}")
        # test 1: there should be non-zero results
        # find the corresponding element on search result page

        result_count = search_result.findResultsCount()
        # driver.close()
        self.log1.warning(f"found {result_count} results for {search_query}")
        assert result_count>0,"No results"

    @file_data("../TestData/testdata.json")
    def test_search_quantity(self,search_query):
        # self.driver = setup
        # test 2: top suggested link contains the searched word atleast 5 times
        lp = LaunchPage(self.driver)
        time.sleep(2)
        search_result = lp.clickSearch(search_query)
        # sp = SearchResultPage(self.driver)
        
        top_link = self.driver.find_element(By.XPATH,"//a[h3]")
        current_window = self.driver.current_window_handle

        search_result.goToResultPage(top_link)

        page_word_count = search_result.countWordOnPage(search_query)
        self.driver.quit()
        assert page_word_count>5

# if __name__=="__main__":
#     unittest.main()