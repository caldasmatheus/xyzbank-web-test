import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage
from pages.managerPage import BankManagerPage

class Test_CT009:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_customer_search(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_manager_page()
        customer_page = CustomerPage(driver=home_page.driver)
        bank_manager_page = BankManagerPage(driver=home_page.driver)
        bank_manager_page.navigate_to_customers()
        customer_page.search_customer('Hermoine')