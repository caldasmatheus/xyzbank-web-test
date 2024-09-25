from selenium import webdriver
from pages.loginPage import LoginPage
from pages.bankManagerPage import BankManagerPage


def test_customer_order():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    bank_manager_page = BankManagerPage(driver)

    login_page.navigate()
    login_page.click_bank_manager_login()
    bank_manager_page.navigate_to_customers()
    bank_manager_page.order_by_first_name()

    first_names = bank_manager_page.get_first_names()
    if first_names == sorted(first_names):
        print("Teste passou: A lista de clientes está ordenada em ordem alfabética.")
        print(first_names)
    else:
        print("Teste falhou: A lista de clientes não está ordenada em ordem alfabética.")
        print(first_names)
    driver.quit()