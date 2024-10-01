import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self, driver=None, browser='chrome'):
        if driver is None:
            if browser == 'chrome':
                chrome_options = Options()

                if os.getenv('HEADLESS'):
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-dev-shm-usage')

                self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = driver

    def is_url(self, url):
        return self.driver.current_url == url

    def wait_element(self, element_tuple, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(element_tuple))

    def close(self):
        self.driver.quit()