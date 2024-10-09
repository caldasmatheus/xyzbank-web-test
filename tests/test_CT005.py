import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage

class Test_CT005:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_view_transaction_list_after_deposit(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_customer_page()
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.select_customer('Hermoine Granger')
        customer_page.click_login_button()
        customer_page.click_transactions_tab()
        customer_page.click_reset_button()
        customer_page.verify_no_transactions()
        customer_page.click_back_button()
        customer_page.click_deposit_tab()
        current_balance = customer_page.verify_balance()
        deposit_value = customer_page.deposit_amount(current_balance + 50000)
        customer_page.verify_message("Deposit Successful")
        customer_page.wait_initial_balance()
        result = customer_page.verify_transaction(deposit_value)
        assert result, "Transação não encontrada com o valor correto e tipo 'Credit'."
