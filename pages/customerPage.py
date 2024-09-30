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

    first_name_field = (By.CSS_SELECTOR, '[ng-model="fName"]')
    last_name_field = (By.CSS_SELECTOR, '[ng-model="lName"]')
    post_code_field = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    add_button = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
    search_customer_field = (By.CSS_SELECTOR, '[ng-model="searchCustomer"]')
    button_delete = (By.CSS_SELECTOR, '[ng-click="deleteCust(cust)"]')

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

    def add_new_customer(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_field)
        )

        self.driver.find_element(*self.first_name_field).send_keys("Iraci")
        self.driver.find_element(*self.last_name_field).send_keys("Teste")
        self.driver.find_element(*self.post_code_field).send_keys("000000-001")

        self.driver.find_element(*self.add_button).click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alert_text = self.driver.switch_to.alert.text

        self.driver.switch_to.alert.accept()

        return 'Customer added successfully with customer' in alert_text

    def navigate_to_search_customers(self):
        customers_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='showCust()']"))
        )
        customers_button.click()

    def search_customer(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_customer_field)
        )

        self.driver.find_element(*self.search_customer_field).send_keys("Harry")

        first_name = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]').text

        return first_name == 'Harry'

    def delete_customer(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.button_delete)
        )

        self.driver.find_element(*self.button_delete).click()

        elements = self.driver.find_elements(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]')

        return not any(elements)
