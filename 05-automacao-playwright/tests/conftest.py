import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.fixture
def login_page_success(page: Page) -> Page:
    login_page = LoginPage(page)
    login_page.base_url()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    return page