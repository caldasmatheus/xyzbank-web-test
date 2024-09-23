from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def click_customer_login(self):
        customer_login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Customer Login')]"))
        )
        customer_login_btn.click()
