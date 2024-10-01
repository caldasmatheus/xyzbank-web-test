import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from conftest import run_all_browser
from pages.customerPage import CustomerPage

class Test_CT003:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_reset_transactions(self, run_all_browser):
        home_page = run_all_browser
        home_page.open_app()
        home_page.go_to_customer_page()
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.select_customer('Hermoine Granger')
        customer_page.click_login_button()
        customer_page.click_transactions_tab()

        customer_page.get_transaction_rows()
        customer_page.click_reset_button()

        if not customer_page.verify_no_transactions():
            time.sleep(2)

        assert customer_page.verify_no_transactions(), "A lista de transações não está vazia após clicar em Reset."
