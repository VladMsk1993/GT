from selenium import webdriver
from pages.GT2.locators.locators import LoginPageLocators
from tests.variables import admin_link, sb_link, login, password
from pages.GT2.pages.login_page import LoginPage
import pytest


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", "regress: mark test to run regress tests."
    )


@pytest.fixture(scope="function")
def browser():
    """Инициализируем браузер."""
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser_auth_srm(browser):
    """Осуществляем авторизацию в SRM."""
    page = LoginPage(browser, admin_link)
    page.open()
    page.login_into_portal(login, password)
    yield browser


@pytest.fixture(scope="function")
def browser_auth_sb(browser):
    """Осуществляем авторизацию в СЭБ."""
    page = LoginPage(browser, sb_link)
    page.open()
    page.login_into_portal(login, password)
    yield browser
