from pages.customerPage import CustomerPage


def test_customer_search(navigate_to_manager):

    home_page = navigate_to_manager
    customer_page = CustomerPage(driver = home_page.driver)
    customer_page.navigate_to_search_customers()

    assert customer_page.search_customer(), 'Ocorreu um erro ao buscar um cliente'

    assert customer_page.delete_customer(), 'Ocorreu um erro ao deletar um cliente'
