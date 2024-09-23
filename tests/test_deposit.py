from selenium import webdriver
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage

def test_deposit():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    customer_page = CustomerPage(driver)

    login_page.navigate()
    login_page.click_customer_login()
    customer_page.select_customer('Hermoine Granger')
    customer_page.click_login_button()
    customer_page.verify_initial_balance('5096')
    customer_page.click_deposit_tab()
    customer_page.deposit_amount(200)
    customer_page.verify_success_message()
    driver.quit()
