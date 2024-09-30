import pytest
from conftest import run_all_browser
from pages.customerPage import CustomerPage
from tests.test_CT010 import Test_CT010

class Test_CT007:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_customer_delete(self, run_all_browser):
        test_add = Test_CT010()
        test_add.test_customer_add(run_all_browser)
        home_page = run_all_browser
        customer_page = CustomerPage(driver=home_page.driver)
        customer_page.search_customer('CRISTIANO')
        customer_page.delete_customer()
        customer_page.search_customer('CRISTIANO')