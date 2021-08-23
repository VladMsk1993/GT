from pages.GT2.pages.header_page import HeaderLinks
from tests.variables import sb_link
import pytest


@pytest.mark.regress
@pytest.mark.header_links
class TestCheckAllHeadersLinks():
    def test_check_links_in_vehicle_page(self, browser_auth_sb):
        page = HeaderLinks(browser_auth_sb, sb_link)
        page.open()
        page.should_check_headers_links_in_vehicle()

    def test_check_links_in_driver_page(self, browser_auth_sb):
        page = HeaderLinks(browser_auth_sb, sb_link)
        page.open()
        page.should_check_headers_links_in_driver()

    def test_check_links_in_counterparty_page(self, browser_auth_sb):
        page = HeaderLinks(browser_auth_sb, sb_link)
        page.open()
        page.should_check_headers_links_in_counterparty()
