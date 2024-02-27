
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.google_search_results_page import SearchResultPage
from Utilities.utils import custLogger

class LaunchPage(BaseDriver):
    # log = custLogger.customlogger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def clickSearch(self, search_query):
        # click on search area, type a query word and press ENTER
        search_box = self.driver.find_element(By.XPATH,"//textarea[@aria-label='Sök']")
        search_box.click()
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)
        search_result_page = SearchResultPage(self.driver)
        # wait for the page to load
        # self.log.warning("opening search results page...")
        time.sleep(2)
        return search_result_page