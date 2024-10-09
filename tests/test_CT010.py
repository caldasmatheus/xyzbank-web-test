import pytest
from faker import Faker
from conftest import run_all_browser
from pages.ManagerPage import ManagerPage

class Test_CT010:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_customer_add(self, run_all_browser):
        faker = Faker('pt_BR')
        home_page = run_all_browser
        home_page.go_to_manager_page()
        manager_page = ManagerPage(driver=home_page.driver)
        manager_page.navigate_to_add_customer()
        first_name = faker.first_name()
        last_name = faker.last_name()
        post_code = faker.postcode()
        manager_page.fill_customer_information(first_name, last_name, post_code)
        manager_page.submit_form()
        alert_verified = manager_page.verify_alert_message('Customer added successfully with customer')
        assert alert_verified, "Teste falhou: A mensagem de alerta não corresponde à esperada."
        manager_page.navigate_to_customers()
        customer_names = manager_page.search_customer(first_name)
        assert customer_names, f"Teste falhou: O cliente '{first_name}' não foi encontrado na lista de clientes."