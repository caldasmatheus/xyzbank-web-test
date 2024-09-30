from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basePage import Base

class CustomerPage(Base):
    SELECT_YOUR_NAME = 'userSelect'
    LOGIN_BTN = "//button[text()='Login']"

    INITIAL_BALANCE = '//div/strong[2]'

    MENU_TRANSACTIONS_BTN = '.center button[ng-click="transactions()"]'
    MENU_DEPOSIT_BTN = "//button[contains(text(), 'Deposit')]"
    MENU_WITHDRAWL_BTN = "//button[contains(text(), 'Withdrawl')]"

    AMOUNT = "//input[@placeholder='amount']"
    DEPOSIT_BTN = "//form[contains(@name, 'myForm')]//button[contains(text(), 'Deposit')]"

    MESSAGE = '.ng-scope span[ng-show="message"]'

    FIRST_NAME = "input[ng-model='fName']"
    LAST_NAME = "input[ng-model='lName']"
    POST_CODE = "input[ng-model='postCd']"
    SEARCH_CUSTOMER = 'input[ng-model="searchCustomer"]'
    DELETE_BTN = '[ng-click="deleteCust(cust)"]'

    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)

    def select_customer(self, customer_name):
        customer_dropdown = self.wait_element((By.NAME, self.SELECT_YOUR_NAME))
        customer_to_select = customer_dropdown.find_element(By.XPATH, f"//option[contains(text(), '{customer_name}')]")
        customer_to_select.click()

    def click_login_button(self):
        self.wait_element((By.XPATH, self.LOGIN_BTN)).click()

    def verify_initial_balance(self):
        initial_amount = self.wait_element((By.XPATH, self.INITIAL_BALANCE))
        balance_text = initial_amount.text
        return int(balance_text)

    def click_deposit_tab(self):
        self.wait_element((By.XPATH, self.MENU_DEPOSIT_BTN)).click()

    def deposit_amount(self, amount):
        self.wait_element((By.XPATH, self.AMOUNT)).send_keys(str(amount))
        self.wait_element((By.XPATH, self.DEPOSIT_BTN)).click()

    def verify_message(self, msg):
        message = self.wait_element((By.CSS_SELECTOR, self.MESSAGE))
        assert message.text == msg
        return msg

    def click_withdrawl_tab(self):
        self.wait_element((By.XPATH, self.MENU_WITHDRAWL_BTN)).click()

    def withdraw_larger_amount(self, valor):
        amount_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='number']"))
        )
        amount_input.send_keys(str(valor))
        withdraw_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//form[contains(@name, 'myForm')]//button[contains(text(), 'Withdraw')]"))
        )
        withdraw_button.click()

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
        assert alert_msg in alert_text
        alert.accept()

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
                print(f"{first_name} found in row.")
                return True
        print(f"{first_name} not found in any row.")
        return False

    def delete_customer(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.DELETE_BTN))
        )
        self.wait_element((By.CSS_SELECTOR, self.DELETE_BTN)).click()
