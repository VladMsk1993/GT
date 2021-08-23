"""
Осуществляем отклонение нового юнита (Контрагента, ТС, водителя) затем отправляем на повторное согласование
и после согласовываем юнита.
"""
from tests.variables import sb_link
from pages.GT2.pages.deny_and_confirm_page import DenyAndConfirmDriver, DenyAndConfirmVehicle, DenyAndConfirmCounterparty
import pytest


#@pytest.mark.
def test_deny_new_driver_and_confirm_after(browser_auth_sb):
    page = DenyAndConfirmDriver(browser_auth_sb, sb_link)
    page.open()
    #page.


#@pytest.mark.
def test_deny_new_vehicle_and_confirm_after(browser_auth_sb):
    page = DenyAndConfirmVehicle(browser_auth_sb, sb_link)
    page.open()
    #page.


#@pytest.mark.
def test_deny_counterparty_and_confirm_after(browser_auth_sb):
    page = DenyAndConfirmCounterparty(browser_auth_sb, sb_link)
    page.open()
    #page.

