from selenium.webdriver.common.by import By

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def countWordOnPage(self,word):
        page_word_count = 0
        page_contents = self.driver.find_elements(By.XPATH,"//p")
        for content in page_contents:
            content_text = content.text
            # print(link_text)
            if word in content_text:
                page_word_count = page_word_count + 1
        return page_word_count
