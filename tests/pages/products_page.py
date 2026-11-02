from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_link = page.locator(".shopping_cart_link")

    def add_item_by_name(self, product_name: str):
        item_container = self.page.locator(".inventory_item").filter(has_text=product_name)
        item_container.locator("button").click()

    def assert_cart_count(self, expected_count: str):
        expect(self.shopping_cart_badge).to_have_text(expected_count)

    def open_cart(self):
        self.shopping_cart_link.click()
