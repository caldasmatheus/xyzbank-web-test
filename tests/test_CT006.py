import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage

class Test_CT006:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_switch_account(self, run_all_browser):
        home_page = run_all_browser
        home_page.go_to_customer_page()
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.select_customer('Hermoine Granger')
        customer_page.click_login_button()
        accounts = customer_page.get_account_options()
        assert len(accounts) > 1, "O usuário não possui mais de uma conta."
        current_account, new_account = customer_page.switch_account(accounts)
        assert new_account != current_account, "A conta não foi alterada."

