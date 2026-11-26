from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

def test_login_success(page: Page):
    login_page = LoginPage(page)
    login_page.base_url()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_locked_user(page: Page):
    login_page = LoginPage(page)
    login_page.base_url()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_alert).to_be_visible()
    expect(login_page.error_alert).to_contain_text("Sorry, this user has been locked out.")

