import json
from pathlib import Path
from playwright.sync_api import Page, expect
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage

DATA_FILE = Path(__file__).parent / "data" / "users.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    test_data = json.load(f)

class TestCart:
    def test_add_product_to_cart(self, page: Page):
        user = test_data["valid_user"]

        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(user["username"], user["password"])

        products_page = ProductsPage(page)
        products_page.add_item_by_name("Sauce Labs Backpack")
        products_page.assert_cart_count("1")

        products_page.open_cart()
        expect(page).to_have_url("https://www.saucedemo.com/cart.html")

        cart_page = CartPage(page)
        cart_page.assert_item_in_cart("Sauce Labs Backpack")
