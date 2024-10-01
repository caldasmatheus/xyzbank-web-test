from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basePage import Base

class ManagerPage(Base):
    ADD_CUSTOMER_BTN = '.center button[ng-click="addCust()"]'
    OPEN_ACCOUNT_BTN = '.center button[ng-click="openAccount()"]'
    CUSTOMERS_BTN = '.center button[ng-click="showCust()"]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
        self.first_name_elements = (By.XPATH, "//table/tbody/tr/td[1]")

    def navigate_to_add_customer(self):
        self.wait_element((By.CSS_SELECTOR, self.ADD_CUSTOMER_BTN)).click()

    def navigate_to_open_account(self):
        self.wait_element((By.CSS_SELECTOR, self.OPEN_ACCOUNT_BTN)).click()

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

    def get_list_customers(self):
        list_customers = self.driver.find_elements(By.CSS_SELECTOR, 'div table[class*="table"] tbody tr td:nth-child(1)')
        return list_customers

    def add_first_name(self):
        self.wait_element((By.CSS_SELECTOR, self.ADD_CUSTOMER_BTN)).click()

    def fill_customer_details(self, first_name: str, last_name: str, postal_code: str) -> None:
        try:
            first_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@ng-model='fName']"))
            )
            first_name_field.send_keys(first_name)

            last_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@ng-model='lName']"))
            )
            last_name_field.send_keys(last_name)

            postal_code_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@ng-model='postCd']"))
            )
            postal_code_field.send_keys(postal_code)

            add_customer_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@type='submit' and normalize-space(text())='Add Customer']"))
            )
            add_customer_button.click()
        except Exception as e:
            print(f"An error occurred while filling customer details: {e}")

    def select_customer_and_currency(self, customer_name, currency):
        customer_select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "userSelect"))
        )
        select_customer = Select(customer_select_element)
        select_customer.select_by_visible_text(customer_name)

        currency_dropdown = Select(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "currency"))
        ))
        currency_dropdown.select_by_value(currency)

        process_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @value='']"))
        )
        process_button.click()


