from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BankPage:
    def __init__(self, driver):
        self.driver = driver

    def click_withdrawl_button(self):
        withdraw_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Withdrawl')]"))
        )
        withdraw_button.click()

    def get_current_balance(self):
        balance_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div/strong[2]"))
        )
        balance_text = balance_element.text
        print(f"Saldo obtido: {balance_text}")
        return int(balance_text)

    def withdraw_larger_amount(self, valor):
        amount_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='number']"))
        )
        amount_input.send_keys(str(valor))
        withdraw_button_final = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//form[contains(@name, 'myForm')]//button[contains(text(), 'Withdraw')]"))
        )
        withdraw_button_final.click()

    def verify_error_message(self):
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Transaction Failed')]"))
        )
        return "Transaction Failed. You can not withdraw amount more than the balance." in error_message.text
