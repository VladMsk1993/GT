from pages.GT2.pages.spectrum_page import CheckInSpectrum
from tests.variables import sb_link
import pytest


@pytest.mark.driver_spectrum
def test_check_driver_in_spectrum(browser_auth_sb):
    page = CheckInSpectrum(browser_auth_sb, sb_link)
    page.open()
    page.sb_should_check_driver_in_spectrum()


@pytest.mark.ts_spectrum
def test_check_vehicle_in_spectrum(browser_auth_sb):
    page = CheckInSpectrum(browser_auth_sb, sb_link)
    page.open()
    page.sb_should_check_vehicle_in_spectrum()
