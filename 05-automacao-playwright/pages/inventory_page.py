from playwright.sync_api import Page

from .base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_backpack_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.remove_backpack_button = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_list = page.locator('[data-test="inventory-item"]')

    def add_backpack_to_cart(self):
        self.add_backpack_button.click()

    def remove_backpack_to_cart(self):
        self.remove_backpack_button.click()

    def go_to_cart(self):
        self.cart_link.click()