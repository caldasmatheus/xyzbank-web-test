from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basePage import Base

class LoginPage(Base):
    def __init__(self, browser):
        super(LoginPage, self).__init__(driver=None, browser=browser)

    def navigate(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def click_customer_login(self):
        customer_login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Customer Login')]"))
        )
        customer_login_btn.click()

    def click_bank_manager_login(self):
        bank_login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Bank Manager Login')]"))
        )
        bank_login_btn.click()
