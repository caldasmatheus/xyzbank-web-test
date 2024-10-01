import pytest
import pages.homePage
from conftest import run_all_browser
from pages.managerPage import managerPage

class test_CT002:

    @pytest.mark.parametrize('run_all_browser', ['chrome'], indirect=True)
    def test_open_customer_account(self, run_all_browser):
        driver = run_all_browser
        home_page = pages.homePage.HomePage(driver)
        home_page.go_to_manager_page()
        manager_page = managerPage(driver=driver)
        manager_page.navigate_to_add_customer()
        manager_page.fill_customer_details(first_name="Alice", last_name="M", postal_code="12345")
        manager_page.navigate_to_open_account()
        manager_page.select_customer_and_currency("Alice M", "Dollar")
