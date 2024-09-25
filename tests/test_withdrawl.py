from selenium import webdriver
from pages.bankPage import BankPage
from pages.loginPage import LoginPage
from pages.customerPage import CustomerPage


def test_withdrawl_greater_than_balance():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    customer_page = CustomerPage(driver)
    bank_page = BankPage(driver)

    login_page.navigate()
    login_page.click_customer_login()
    customer_page.select_customer('Harry Potter')
    customer_page.click_login_button()
    bank_page.click_withdrawl_button()

    saldo_atual = bank_page.get_current_balance()
    bank_page.withdraw_larger_amount(saldo_atual + 100)

    if bank_page.verify_error_message():
        print("O teste passou: A mensagem de erro apareceu como esperado.")
    else:
        print("O teste falhou: A mensagem de erro não apareceu.")

    driver.quit()