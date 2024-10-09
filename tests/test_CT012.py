import pytest
from conftest import run_all_browser
from pages.ManagerPage import ManagerPage

class Test_CT012:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_add_duplicate_customer(self, run_all_browser):
        existing_first_name = "Hermoine"
        existing_last_name = "Granger"
        existing_post_code = "1234"

        home_page = run_all_browser
        home_page.go_to_manager_page()

        manager_page = ManagerPage(driver=home_page.driver)

        manager_page.navigate_to_add_customer()

        manager_page.fill_customer_information(existing_first_name, existing_last_name, existing_post_code)
        manager_page.submit_form()
        alert_verified = manager_page.verify_alert_message('Customer added successfully with customer')
        assert alert_verified, "Teste falhou: A mensagem de alerta não corresponde à esperada."

        manager_page.navigate_to_add_customer()
        manager_page.fill_customer_information(existing_first_name, existing_last_name, existing_post_code)
        manager_page.submit_form()
        alert_verified = manager_page.verify_alert_message('Please check the details. Customer may be duplicate.')
        assert alert_verified, "Teste falhou: A mensagem de alerta não corresponde à esperada."
