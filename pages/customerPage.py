from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from pages.basePage import Base

class CustomerPage(Base):

    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)

    def select_customer(self, customer_name):
        customer_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userSelect"))
        )
        customer_to_select = customer_dropdown.find_element(By.XPATH, f"//option[contains(text(), '{customer_name}')]")
        customer_to_select.click()

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
        )
        login_button.click()

    def verify_initial_balance(self):
        initial_amount = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div/strong[2]"))
        )
        balance_text = initial_amount.text
        print(f"Saldo obtido: {balance_text}")
        return int(balance_text)

    def click_deposit_tab(self):
        deposit_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Deposit')]"))
        )
        deposit_tab.click()

    def deposit_amount(self, amount):
        deposit_amount_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='amount']"))
        )
        deposit_amount_input.send_keys(str(amount))
        deposit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//form[contains(@name, 'myForm')]//button[contains(text(), 'Deposit')]"))
        )
        deposit_button.click()

    def verify_success_message(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Deposit Successful')]"))
        )
        assert success_message.text == "Deposit Successful"

    def add_new_customer(self):
        first_name_field = (By.CSS_SELECTOR, '[ng-model="fName"]')
        last_name_field = (By.CSS_SELECTOR, '[ng-model="lName"]')
        post_code_field = (By.CSS_SELECTOR, '[ng-model="postCd"]')
        add_button  = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(first_name_field)
        )

        self.driver.find_element(*first_name_field).send_keys("Iraci")
        self.driver.find_element(*last_name_field).send_keys("Teste")
        self.driver.find_element(*post_code_field).send_keys("000000-001")

        self.driver.find_element(*add_button).click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alert_text = self.driver.switch_to.alert.text

        self.driver.switch_to.alert.accept()

        #pra ver em tela descomentar o time
        # time.sleep(5000)

        return 'Customer added successfully with customer' in alert_text

    def navigate_to_search_customers(self):
        customers_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='showCust()']"))
        )
        customers_button.click()

    def search_customer(self):
        search_customer = (By.CSS_SELECTOR, '[ng-model="searchCustomer"]')

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(search_customer)
        )

        self.driver.find_element(*search_customer).send_keys("Harry")

        first_name = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]').text

        # pra ver em tela descomentar o time
        # time.sleep(5)

        return first_name == 'Harry'

    def delete_customer(self):
        button_delete = (By.CSS_SELECTOR, '[ng-click="deleteCust(cust)"]')

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(button_delete)
        )

        self.driver.find_element(*button_delete).click()

        elements = self.driver.find_elements(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]')

        return not any(elements)