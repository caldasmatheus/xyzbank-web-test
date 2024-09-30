from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basePage import Base

class BankManagerPage(Base):
    ADD_CUSTOMER_BTN = '.center button[ng-click="addCust()"]'
    OPEN_ACCOUNT_BTN = '.center button[ng-click="openAccount()"]'
    CUSTOMERS_BTN = '.center button[ng-click="showCust()"]'

    def __init__(self, driver):
        super(BankManagerPage, self).__init__(driver=driver)
        self.first_name_elements = (By.XPATH, "//table/tbody/tr/td[1]")

    def navigate_to_add_customer(self):
        self.wait_element((By.CSS_SELECTOR, self.ADD_CUSTOMER_BTN)).click()

    def navigate_to_open_account(self):
        self.wait_element((By.CSS_SELECTOR, self. OPEN_ACCOUNT_BTN)).click()

    def navigate_to_customers(self):
        self.wait_element((By.CSS_SELECTOR, self.CUSTOMERS_BTN)).click()

    def order_by_first_name(self):
        last_name_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//table/thead/tr/td[2]"))
        )
        last_name_button.click()

        first_name_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//table/thead/tr/td[1]"))
        )
        first_name_button.click()

    def get_first_names(self):
        elements = self.driver.find_elements(*self.first_name_elements)
        first_names = []
        for element in elements:
            first_names.append(element.text)
        return first_names

    def navigate_to_add_customers(self):
        customers_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='addCust()']"))
        )
        customers_button.click()