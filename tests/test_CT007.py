import pytest
from conftest import run_all_browser
from pages.ManagerPage import ManagerPage

class Test_CT007:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_customer_delete(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_manager_page()
        manager_page = ManagerPage(driver=home_page.driver)
        manager_page.navigate_to_customers()
        first_name = manager_page.get_customer_name(indice=1)
        assert manager_page.search_customer(first_name), f"Teste falhou: O cliente '{first_name}' deveria existir antes da exclusão."
        manager_page.search_customer(first_name)
        manager_page.delete_customer()
        assert not manager_page.search_customer(first_name), f"Teste falhou: O cliente '{first_name}' ainda existe após a exclusão."