from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.basePage import Base

class HomePage(Base):
    HOME_BTN = "//button[contains(text(), 'Home')]"
    CUSTOMER_BTN = '.center button[ng-click="customer()"]'
    MANAGER_BTN = '.center button[ng-click="manager()"]'
    BASE_URL = 'https://globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def __init__(self, browser):
        super(HomePage, self).__init__(driver=None, browser=browser)

    def open_app(self):
        self.driver.get(self.BASE_URL)

    def go_to_customer_page(self):
        customer_login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.CUSTOMER_BTN))
        )
        customer_login_btn.click()

    def go_to_manager_page(self):
        manager_login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.MANAGER_BTN))
        )
        manager_login_btn.click()

    def go_to_home_page(self):
        home_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_BTN))
        )
        home_btn.click()
