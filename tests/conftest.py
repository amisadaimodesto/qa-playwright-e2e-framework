import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "locale": "pt-BR",
    }

@pytest.fixture
def page(page: Page, request):
    yield page
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        screenshot_path = f"reports/screenshot_fail_{request.node.name}.png"
        page.screenshot(path=screenshot_path, full_page=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
