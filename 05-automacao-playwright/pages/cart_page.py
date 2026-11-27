from playwright.sync_api import Page

from .base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.checkout_button = page.locator('[data-test="checkout"]')

    def proceed_to_checkout(self):
        self.checkout_button.click()