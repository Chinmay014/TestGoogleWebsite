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
    
    @data(*custLogger.read_data_from_csv("F:\\DesktopC\\PythonUltimateCourse\\SoftwareTesting\\TestGoogleWebsite\\TestData\\testdata.csv"))
    @unpack
    def test_search_results(self,search_query):
        self.log1.info("############# Test 1 ##################",exc_info=0)
        lp = LaunchPage(self.driver)
        self.log1.info(f"Searching for {search_query}...")
        search_result = lp.clickSearch(search_query)
        # test 1: there should be non-zero results

        result_count = search_result.findResultsCount()
        # driver.close()
        self.driver.quit()
        self.log1.info(f"found {result_count} results for {search_query}")
        self.log1.info("###################################")
        assert result_count>0,"No results"

    @data(*custLogger.read_data_from_csv("F:\\DesktopC\\PythonUltimateCourse\\SoftwareTesting\\TestGoogleWebsite\\TestData\\testdata.csv"))
    @unpack
    def test_search_quantity(self,search_query):
        # self.driver = setup
        # test 2: top suggested link contains the searched word atleast 5 times
        self.log1.info("############# Test 2 ##################",exc_info=0)
        lp = LaunchPage(self.driver)
        time.sleep(2)
        search_result = lp.clickSearch(search_query)
        # sp = SearchResultPage(self.driver)
        self.log1.info("search page loaded")
        top_link = self.driver.find_element(By.XPATH,"//a[h3]")
        self.log1.info("Navigating to top search result")
        current_window = self.driver.current_window_handle

        search_result.goToResultPage(top_link)

        page_word_count = search_result.countWordOnPage(search_query)
        self.driver.quit()
        self.log1.info(f"found {page_word_count} words matching {search_query}")
        self.log1.info("###################################")
        assert page_word_count>5

# if __name__=="__main__":
#     unittest.main()