import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage
from pages.managerPage import BankManagerPage

class Test_CT010:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_customer_add(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_manager_page()
        customer_page = CustomerPage(driver=home_page.driver)
        bank_manager_page = BankManagerPage(driver=home_page.driver)
        bank_manager_page.navigate_to_add_customer()
        customer_page.fill_customer_information('CRISTIANO', 'RONALDO', '12345-000')
        customer_page.submit_form()
        customer_page.verify_alert_message('Customer added successfully with customer')
        bank_manager_page.navigate_to_customers()
        customer_page.search_customer('CRISTIANO')