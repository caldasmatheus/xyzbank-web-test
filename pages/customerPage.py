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

    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)

    def select_customer(self, customer_name):
        customer_dropdown = self.wait_element((By.NAME, self.SELECT_YOUR_NAME))
        customer_to_select = customer_dropdown.find_element(By.XPATH, f"//option[contains(text(), '{customer_name}')]")
        customer_to_select.click()

    def click_login_button(self):
        self.wait_element((By.XPATH, self.LOGIN_BTN)).click()

    def verify_balance(self):
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
