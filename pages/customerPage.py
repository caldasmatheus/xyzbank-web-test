from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerPage:
    def __init__(self, driver):
        self.driver = driver

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

    def verify_initial_balance(self, initial_amount):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//strong[contains(text(), '{initial_amount}')]"))
        )

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

        deposit_button = self.driver.find_element(By.XPATH, "//button[text()='Deposit']")
        deposit_button.click()

    def verify_success_message(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Deposit Successful')]"))
        )
        assert success_message.text == "Deposit Successful"
