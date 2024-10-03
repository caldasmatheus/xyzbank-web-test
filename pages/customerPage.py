import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basePage import Base

class CustomerPage(Base):
    SELECT_YOUR_NAME = 'userSelect'
    LOGIN_BTN = "//button[text()='Login']"

    ACCOUNT_DROPDOWN = "accountSelect"
    INITIAL_BALANCE = '//div/strong[2]'

    MENU_TRANSACTIONS_BTN = "//button[contains(text(), 'Transactions')]"
    MENU_DEPOSIT_BTN = "//button[contains(text(), 'Deposit')]"
    MENU_WITHDRAWL_BTN = "//button[contains(text(), 'Withdrawl')]"

    TRANSACTIONS_TABLE = "//table[@class='table table-bordered table-striped']"
    MENU_TRANSACTIONS_BTN_RESET = "//button[contains(text(), 'Reset')]"
    MENU_TRANSACTIONS_BTN_BACK = "//button[contains(text(), 'Back')]"

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

    def wait_initial_balance(self):
        self.wait_element((By.XPATH, self.INITIAL_BALANCE))
        time.sleep(1)

    def click_deposit_tab(self):
        self.wait_element((By.XPATH, self.MENU_DEPOSIT_BTN)).click()

    def deposit_amount(self, amount):
        self.wait_element((By.XPATH, self.AMOUNT)).send_keys(str(amount))
        self.wait_element((By.XPATH, self.DEPOSIT_BTN)).click()
        return amount

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
        return valor

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

    def click_transactions_tab(self):
        self.wait_element((By.XPATH, self.MENU_TRANSACTIONS_BTN)).click()

    def get_transaction_rows(self):
        transactions_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='table table-bordered table-striped']/tbody"))
        )
        transaction_rows = transactions_table.find_elements(By.TAG_NAME, 'tr')
        return transaction_rows

    def click_reset_button(self):
        self.wait_element((By.XPATH, self.MENU_TRANSACTIONS_BTN_RESET)).click()

    def click_back_button(self):
        self.wait_element((By.XPATH, self.MENU_TRANSACTIONS_BTN_BACK)).click()

    def verify_transaction(self, expected_amount):
        self.wait_element((By.XPATH, self.MENU_TRANSACTIONS_BTN)).click()
        transactions_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.TRANSACTIONS_TABLE)))

        rows = transactions_table.find_elements(By.XPATH, ".//tbody/tr")

        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            amount = columns[1].text.strip()
            transaction_type = columns[2].text.strip().lower()
            if f"{expected_amount}" == amount and transaction_type == "credit":
                return True
        return False

    def verify_no_transactions(self):
        transaction_rows = self.get_transaction_rows()
        return len(transaction_rows) == 0

    def enter_customer_details(self, first_name, last_name, post_code):
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
        )
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        last_name_input.send_keys(last_name)

        post_code_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Post Code']")
        post_code_input.send_keys(post_code)

    def handle_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def verify_welcome_title(self, msg):
        message = self.wait_element((By.XPATH, f"//strong[contains(text(), ' Welcome ')]/span[contains(text(), '{msg}')]"))
        assert message.text == msg
        return msg

    def get_account_options(self):
        account_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "accountSelect"))
        )
        return account_dropdown.find_elements(By.TAG_NAME, 'option')

    def switch_account(self, accounts):
        current_account = accounts[0].text
        accounts[1].click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "accountSelect"), accounts[1].text)
        )
        return current_account, accounts[1].text
