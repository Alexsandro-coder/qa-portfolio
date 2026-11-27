from playwright.sync_api import Page, expect

from pages import CartPage, InventoryPage


def test_add_item_to_cart(login_page_success: Page):
    """VF-15: Adicionar produto ao carrinho e validar badge e item listado."""
    inventory_page = InventoryPage(login_page_success)
    cart_page = CartPage(login_page_success)

    inventory_page.add_backpack_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.go_to_cart()
    expect(login_page_success).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart_page.title).to_have_text("Your Cart")
    expect(cart_page.item_name).to_have_text("Sauce Labs Backpack")


def test_remove_item_from_cart(login_page_success: Page):
    """VF-16: Remover produto do carrinho e validar estado vazio."""
    inventory_page = InventoryPage(login_page_success)
    cart_page = CartPage(login_page_success)

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    expect(login_page_success).to_have_url("https://www.saucedemo.com/cart.html")

    cart_page.remove_backpack()
    expect(cart_page.item_name).to_have_count(0)
    expect(inventory_page.cart_badge).not_to_be_visible()