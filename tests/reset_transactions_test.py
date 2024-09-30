from selenium import webdriver
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.transactions_page import TransactionsPage

def test_reset_transactions():
    driver = webdriver.Chrome()

    try:
        login_page = LoginPage(driver)
        customer_page = CustomerPage(driver)
        name_client = 'Hermoine Granger'

        transactions_page = TransactionsPage(driver)
        login_page.navigate()
        login_page.click_customer_login()
        customer_page.select_customer(name_client)
        customer_page.click_login_button()
        transactions_page.click_transactions_tab()
        transaction_rows = transactions_page.get_transaction_rows()
        assert len(transaction_rows) > 0, "Nenhuma transação encontrada para o cliente."
        transactions_page.click_reset_button()
        transactions_page.verify_no_transactions()

    finally:
        driver.quit()
