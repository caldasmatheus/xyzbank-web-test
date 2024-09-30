from selenium import webdriver
from pages.bankManagerPage import BankManagerPage
from pages.customerPage import CustomerPage


def test_customer_add(login_bank_manager):

    login_page = login_bank_manager
    bank_manager_page = BankManagerPage(login_page.driver)
    bank_manager_page.navigate_to_add_customers()
    customer_page = CustomerPage(driver = login_page.driver)

    assert customer_page.add_new_customer(), 'Ocorreu um erro ao adicionar um cliente'