import pytest
from conftest import run_all_browser
from pages.managerPage import BankManagerPage

class Test_CT008:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_first_name_customer_order(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_manager_page()
        bank_manager_page = BankManagerPage(driver=home_page.driver)
        bank_manager_page.navigate_to_customers()
        bank_manager_page.order_by_first_name()
        first_names = bank_manager_page.get_first_names()
        if first_names == sorted(first_names):
            print("Teste passou: A lista de clientes está ordenada em ordem alfabética.")
            print(first_names)
        else:
            print("Teste falhou: A lista de clientes não está ordenada em ordem alfabética.")
            print(first_names)