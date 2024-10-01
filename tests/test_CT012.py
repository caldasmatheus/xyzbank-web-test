import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage
from pages.ManagerPage import ManagerPage

class Test_CT012:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_add_duplicate_customer(self, run_all_browser):
        existing_first_name = "Hermoine"
        existing_last_name = "Granger"
        existing_post_code = "1234"

        home_page = run_all_browser
        home_page.go_to_manager_page()

        customer_page = CustomerPage(driver=home_page.driver)
        manager_page = ManagerPage(driver=home_page.driver)

        manager_page.navigate_to_add_customer()

        customer_page.enter_customer_details(existing_first_name, existing_last_name, existing_post_code)
        customer_page.submit_form()
        customer_page.handle_alert()

        manager_page.navigate_to_add_customer()
        customer_page.enter_customer_details(existing_first_name, existing_last_name, existing_post_code)
        customer_page.submit_form()
        alert_text = customer_page.handle_alert()
        assert "Please check the details. Customer may be duplicate." in alert_text, f"Mensagem inesperada: {alert_text}"
