from selenium import webdriver
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.withdraw_page import WithdrawPage

def test_withdrawal():
    driver = webdriver.Chrome()

    try:
        login_page = LoginPage(driver)
        customer_page = CustomerPage(driver)
        withdraw_page = WithdrawPage(driver)
        initial_balance = '5096'
        withdrawal_amount = 40
        name_client = 'Hermoine Granger'

        login_page.navigate()
        login_page.click_customer_login()
        customer_page.select_customer(name_client)

        customer_page.click_login_button()
        customer_page.verify_initial_balance(initial_balance)
        withdraw_page.click_withdraw_tab()

        withdraw_page.enter_withdrawal_amount(withdrawal_amount)
        withdraw_page.click_withdraw_button()
        withdraw_page.verify_success_transaction_message()

    finally:
        driver.quit()
