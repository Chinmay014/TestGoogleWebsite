from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
import re, time


class SearchResultPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def findResultsCount(self):
        result_element = self.driver.find_element(By.XPATH, "//div[@id='result-stats']")
        result_text = result_element.text
        print(result_text)
        numbers = re.findall(r'\d{1,3}(?:\s?\d{3})*', result_text)
        print(numbers)
        result_count = int(numbers[0].replace(' ',''))
        return result_count

    def goToResultPage(self,result_link):
        self.driver.execute_script("window.open(arguments[0].getAttribute('href'),'_blank');",result_link)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
