import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage

class Test_CT001:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_deposit(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_customer_page()
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.select_customer('Hermoine Granger')
        customer_page.click_login_button()
        customer_page.click_deposit_tab()
        current_balance = customer_page.verify_initial_balance()
        balance = customer_page.deposit_amount(current_balance + 100)
        customer_page.verify_message("Deposit Successful")
        assert balance == current_balance + 100, f"Teste falhou: Esperado {current_balance + 100}, encontrado {balance}"
