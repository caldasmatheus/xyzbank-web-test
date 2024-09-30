import pytest
from pages.homePage import HomePage

def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser to run tests.')

@pytest.fixture
def run_all_browser(all_browser):
    home_page = HomePage(browser=all_browser)
    home_page.open_app()
    yield home_page
    home_page.close()

@pytest.fixture
def open_browser(request):
    selected_browser = request.config.getoption('browser_selenium').lower()
    home_page = HomePage(browser=selected_browser)
    home_page.open_app()
    yield home_page
    home_page.close()

@pytest.fixture
def navegate_to_home(open_browser):
    home_page = open_browser
    yield home_page
