import json
from pathlib import Path
import pytest
from playwright.sync_api import Page, expect
from tests.pages.login_page import LoginPage

DATA_FILE = Path(__file__).parent / "data" / "users.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    test_data = json.load(f)

class TestLogin:
    def test_successful_login(self, page: Page):
        user = test_data["valid_user"]
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(user["username"], user["password"])
        expect(page).to_have_url(f"https://www.saucedemo.com{user['expected_url_path']}")
        expect(page.locator(".title")).to_have_text(user["expected_header"])

    def test_locked_out_user(self, page: Page):
        user = test_data["locked_user"]
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(user["username"], user["password"])
        login_page.assert_error_contains(user["expected_error"])
