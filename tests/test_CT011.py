import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage

class Test_CT011:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_withdrawl_greater_than_balance(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_customer_page()
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.select_customer('Hermoine Granger')
        customer_page.click_login_button()
        customer_page.click_withdrawl_tab()
        current_balance = customer_page.verify_initial_balance()
        balance = customer_page.withdraw_larger_amount(current_balance + 50000)
        customer_page.verify_message('Transaction Failed. You can not withdraw amount more than the balance.')
        new_balance = balance - 50000
        value_final = customer_page.verify_initial_balance()
        assert new_balance == value_final, f"Teste falhou: Esperado {value_final}, encontrado {new_balance}"