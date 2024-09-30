from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransactionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_transactions_tab(self):
        transactions_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Transactions')]"))
        )
        transactions_tab.click()

    def get_transaction_rows(self):
        transactions_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='table table-bordered table-striped']/tbody"))
        )
        transaction_rows = transactions_table.find_elements(By.TAG_NAME, 'tr')
        return transaction_rows

    def click_reset_button(self):
        reset_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reset')]"))
        )
        reset_button.click()

    def verify_no_transactions(self):
        transaction_rows = self.get_transaction_rows()
        assert len(transaction_rows) == 0, "Ainda há transações após clicar em Reset."

