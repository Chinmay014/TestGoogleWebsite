from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as ffService
from selenium.webdriver.edge.service import Service as edService
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture(scope="class")
def setup(request,browser):
    if browser=="chrome":
        service = ChromeService()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser=="ff":
        service = ffService()
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service,options=options)
    else:
        service = edService()
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service,options=options)
    
    driver.get('https://google.com/')
    WebDriverWait(driver,5)
    driver.maximize_window()

    # agree to cookies
    driver.find_element(By.XPATH,"//button//div[contains(text(), 'Godkänn alla')]").click() 
    request.cls.driver = driver
    yield driver
    # driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")