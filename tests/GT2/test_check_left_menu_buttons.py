from pages.GT2.pages.left_menu_page import CheckLeftMenu
from tests.variables import sb_link
import pytest


@pytest.mark.left_menu
def test_check_buttons_in_left_menu(browser_auth_sb):
    page = CheckLeftMenu(browser_auth_sb, sb_link)
    page.open()
    page.should_check_buttons_in_left_menu()
