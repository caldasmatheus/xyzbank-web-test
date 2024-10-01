import pytest
from faker import Faker
from conftest import run_all_browser
from pages.customerPage import CustomerPage
from pages.ManagerPage import ManagerPage

class Test_CT002:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_open_customer_account(self, run_all_browser):
        faker = Faker('pt_BR')
        home_page = run_all_browser
        home_page.go_to_manager_page()
        customer_page = CustomerPage(driver=home_page.driver)
        manager_page = ManagerPage(driver=home_page.driver)
        manager_page.navigate_to_add_customer()
        first_name = faker.first_name()
        last_name = faker.last_name()
        post_code = faker.postcode()
        customer_page.fill_customer_information(first_name, last_name, post_code)
        customer_page.submit_form()
        alert_verified = customer_page.verify_alert_message('Customer added successfully with customer')
        assert alert_verified, "Teste falhou: A mensagem de alerta não corresponde à esperada."
        manager_page.navigate_to_open_account()
        complete_name = first_name + ' ' + last_name
        manager_page.select_customer_and_currency(complete_name, 'Dollar')
        alert_verified = customer_page.verify_alert_message('Account created successfully with account Number')
        assert alert_verified, "Teste falhou: A mensagem de alerta não corresponde à esperada."
        home_page.go_to_home_page()
        home_page.go_to_customer_page()
        customer_page.select_customer(complete_name)
        customer_page.click_login_button()
        verify_client = customer_page.verify_welcome_title(complete_name)
        assert verify_client, f"Teste falhou: O cliente '{verify_client}' não tem conta ativa"
