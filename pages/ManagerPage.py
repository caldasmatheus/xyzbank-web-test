from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basePage import Base

class ManagerPage(Base):
    ADD_CUSTOMER_BTN = '.center button[ng-click="addCust()"]'
    OPEN_ACCOUNT_BTN = '.center button[ng-click="openAccount()"]'
    CUSTOMERS_BTN = '.center button[ng-click="showCust()"]'

    FIRST_NAME = "input[ng-model='fName']"
    LAST_NAME = "input[ng-model='lName']"
    POST_CODE = "input[ng-model='postCd']"

    SEARCH_CUSTOMER = 'input[ng-model="searchCustomer"]'
    DELETE_BTN = '[ng-click="deleteCust(cust)"]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
        self.first_name_elements = (By.XPATH, "//table/tbody/tr/td[1]")

    def navigate_to_add_customer(self):
        self.wait_element((By.CSS_SELECTOR, self.ADD_CUSTOMER_BTN)).click()

    def navigate_to_open_account(self):
        self.wait_element((By.CSS_SELECTOR, self.OPEN_ACCOUNT_BTN)).click()

    def navigate_to_customers(self):
        self.wait_element((By.CSS_SELECTOR, self.CUSTOMERS_BTN)).click()

    def fill_customer_information(self, first_name, last_name, post_code):
        self.wait_element((By.CSS_SELECTOR, self.FIRST_NAME)).send_keys(first_name)
        self.wait_element((By.CSS_SELECTOR, self.LAST_NAME)).send_keys(last_name)
        self.wait_element((By.CSS_SELECTOR, self.POST_CODE)).send_keys(post_code)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//form[contains(@name, 'myForm')]//button[contains(text(), 'Add Customer')]"))
        )
        submit_button.click()

    def verify_alert_message(self, alert_msg):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_msg in alert_text

    def select_customer_and_currency(self, customer, currency):
        self.wait_element((By.ID, "userSelect")).send_keys(customer)
        self.wait_element((By.ID, "currency")).send_keys(currency)
        self.wait_element((By.XPATH, "//button[@type='submit' and @value='']")).click()

    def get_customer_name(self, indice):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f'div table[class*="table"] tbody tr:nth-child({indice}) td:nth-child(1)'))
        )
        customer_name = element.text
        return customer_name

    def search_customer(self,first_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.SEARCH_CUSTOMER))
        )
        search_input = self.wait_element((By.CSS_SELECTOR, self.SEARCH_CUSTOMER))
        search_input.clear()
        search_input.send_keys(first_name)
        customers_table = self.driver.find_element(By.TAG_NAME, "table")
        rows = customers_table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if any(first_name in cell.text for cell in cells):
                return True
        return False

    def delete_customer(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.DELETE_BTN))
        )
        self.wait_element((By.CSS_SELECTOR, self.DELETE_BTN)).click()

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
