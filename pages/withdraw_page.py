from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WithdrawPage:
    def __init__(self, driver):
        self.driver = driver

    def click_withdraw_tab(self):
        withdraw_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Withdrawl')]"))
        )
        withdraw_tab.click()

    def enter_withdrawal_amount(self, amount):
        withdrawal_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='amount']"))
        )
        withdrawal_input.send_keys(str(amount))


    def click_withdraw_button(self):
        withdraw_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Withdraw']"))
        )
        withdraw_button.click()

    def verify_balance_updated(self, expected_balance):
        updated_balance = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//strong[contains(text(), '" + expected_balance + "')]"))
        )
        assert updated_balance.text == expected_balance, f"O saldo esperado era {expected_balance}, mas o saldo atual é {updated_balance.text}"

    def verify_success_transaction_message(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Transaction successful')]"))
        )
        assert success_message.text == "Transaction successful"

