import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage
from pages.managerPage import managerPage

class Test_CT009:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_customer_search(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_manager_page()
        customer_page = CustomerPage(driver=home_page.driver)
        bank_manager_page = managerPage(driver=home_page.driver)
        bank_manager_page.navigate_to_customers()
        first_name = customer_page.get_customer_name(indice=1)
        customer_names = customer_page.search_customer(first_name)
        assert customer_names, f"Teste falhou: O cliente '{first_name}' não foi encontrado na lista de clientes."