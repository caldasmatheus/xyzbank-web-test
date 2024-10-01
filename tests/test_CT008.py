import time

import pytest
from conftest import run_all_browser
from pages.managerPage import managerPage

class Test_CT008:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_first_name_customer_order(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_manager_page()
        bank_manager_page = managerPage(driver=home_page.driver)
        bank_manager_page.navigate_to_customers()
        bank_manager_page.order_by_first_name()
        first_names = bank_manager_page.get_first_names()
        list_customer = bank_manager_page.get_list_customers()
        customer_names = []
        for name in list_customer:
            customer_names.append(name.text.strip())

        assert first_names == customer_names, (
            "Teste falhou: A lista de clientes não está ordenada em ordem alfabética. "
            f"Nomes extraídos: {first_names}"
        )