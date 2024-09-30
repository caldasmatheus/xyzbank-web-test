import pytest

from pages.loginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser to run tests.')


@pytest.fixture
def run_all_browser(all_browser):
    login_p = LoginPage(browser=all_browser)
    login_p.navigate()
    yield login_p
    login_p.close()


@pytest.fixture
def open_browser(request):
    selected_browser = request.config.getoption('browser_selenium').lower()
    login_page = LoginPage(browser=selected_browser)
    login_page.navigate()
    yield login_page
    login_page.close()

@pytest.fixture
def login_bank_manager(open_browser):
    login_page = open_browser
    login_page.click_bank_manager_login()
    yield login_page
