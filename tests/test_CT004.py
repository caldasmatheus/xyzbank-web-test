import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage


class Test_CT004:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_withdraw_success(self, run_all_browser):
        home_page = run_all_browser
        home_page.open_app()
        home_page.go_to_customer_page()
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.select_customer('Hermoine Granger')
        customer_page.click_login_button()

        initial_balance = customer_page.verify_initial_balance()

        customer_page.click_withdrawl_tab()
        amount_to_withdraw = 40
        customer_page.withdraw_larger_amount(amount_to_withdraw)
        updated_balance = customer_page.verify_initial_balance()
        expected_balance = initial_balance - amount_to_withdraw

        assert updated_balance == expected_balance, f"Teste falhou: Esperado {expected_balance}, encontrado {updated_balance}"
