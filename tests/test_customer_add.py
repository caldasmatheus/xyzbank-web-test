from pages.managerPage import BankManagerPage
from pages.customerPage import CustomerPage


def test_customer_add(navigate_to_manager):

    home_page = navigate_to_manager
    bank_manager_page = BankManagerPage(home_page.driver)
    bank_manager_page.navigate_to_add_customers()
    customer_page = CustomerPage(driver = home_page.driver)

    assert customer_page.add_new_customer(), 'Ocorreu um erro ao adicionar um cliente'