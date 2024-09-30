from selenium import webdriver
from pages.loginPage import LoginPage
from pages.customerPage import CustomerPage

def test_deposit():
    login_page = LoginPage('chrome')
    driver = login_page.driver
    customer_page = CustomerPage(driver)

    login_page.navigate()
    login_page.click_customer_login()
    customer_page.select_customer('Hermoine Granger')
    customer_page.click_login_button()
    customer_page.click_deposit_tab()

    saldo_atual = customer_page.verify_initial_balance()
    customer_page.deposit_amount(saldo_atual + 100)
    customer_page.verify_success_message()
    driver.quit()
