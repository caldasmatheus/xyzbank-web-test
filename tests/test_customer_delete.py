from selenium import webdriver
from pages.bankManagerPage import BankManagerPage
from pages.customerPage import CustomerPage


def test_customer_search(login_bank_manager):

    login_page = login_bank_manager
    customer_page = CustomerPage(driver = login_page.driver)
    customer_page.navigate_to_search_customers()

    assert customer_page.search_customer(), 'Ocorreu um erro ao buscar um cliente'

    assert customer_page.delete_customer(), 'Ocorreu um erro ao deletar um cliente'
