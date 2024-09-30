import pytest
from faker import Faker
from conftest import run_all_browser
from pages.customerPage import CustomerPage
from pages.managerPage import managerPage

class Test_CT010:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_customer_add(self, run_all_browser):
        faker = Faker('pt_BR')
        home_page = run_all_browser
        home_page.go_to_manager_page()
        customer_page = CustomerPage(driver=home_page.driver)
        add_customer_page = managerPage(driver=home_page.driver)
        add_customer_page.navigate_to_add_customer()
        first_name = faker.first_name()
        last_name = faker.last_name()
        post_code = faker.postcode()
        customer_page.fill_customer_information(first_name, last_name, post_code)
        customer_page.submit_form()
        alert_verified = customer_page.verify_alert_message('Customer added successfully with customer')
        assert alert_verified, "Teste falhou: A mensagem de alerta não corresponde à esperada."
        add_customer_page.navigate_to_customers()
        customer_names = customer_page.search_customer(first_name)
        assert customer_names, f"Teste falhou: O cliente '{first_name}' não foi encontrado na lista de clientes."