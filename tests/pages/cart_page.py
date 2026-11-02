from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")

    def assert_item_in_cart(self, product_name: str):
        item = self.cart_items.filter(has=self.page.locator(".inventory_item_name", has_text=product_name))
        expect(item).to_be_visible()
