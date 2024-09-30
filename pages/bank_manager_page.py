from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BankManagerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_bank_manager_login(self):
        bank_manager_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Bank Manager Login')]"))
        )
        bank_manager_btn.click()

    def click_add_customer(self):
        add_customer_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Customer')]"))
        )
        add_customer_btn.click()

    def enter_customer_details(self, first_name, last_name, post_code):
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
        )
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        last_name_input.send_keys(last_name)

        post_code_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Post Code']")
        post_code_input.send_keys(post_code)

    def click_add_customer_button(self):
        add_customer_btn = self.driver.find_element(By.XPATH, "//button[text()='Add Customer']")
        add_customer_btn.click()

    def handle_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text
