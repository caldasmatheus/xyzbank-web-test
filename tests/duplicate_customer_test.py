from selenium import webdriver
from pages.bank_manager_page import BankManagerPage
from pages.login_page import LoginPage


def test_duplicate_customer():
    driver = webdriver.Chrome()

    try:
        login_page = LoginPage(driver)
        bank_manager_page = BankManagerPage(driver)
        first_name = "Hermoine"
        last_name = "Granger"
        post_code = "1234"

        login_page.navigate()
        bank_manager_page.click_bank_manager_login()
        bank_manager_page.click_add_customer()
        bank_manager_page.enter_customer_details(first_name, last_name, post_code)
        bank_manager_page.click_add_customer_button()
        bank_manager_page.handle_alert()
        bank_manager_page.click_add_customer()
        bank_manager_page.enter_customer_details(first_name, last_name, post_code)
        bank_manager_page.click_add_customer_button()
        alert_text = bank_manager_page.handle_alert()
        assert "Please check the details. Customer may be duplicate." in alert_text, f"Mensagem inesperada: {alert_text}"

    finally:
        driver.quit()
