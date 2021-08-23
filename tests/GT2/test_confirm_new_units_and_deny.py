"""
Осуществляем согласование нового юнита (Контрагента, ТС, водителя) затем отправляем на повторное согласование
и после откланяем юнита.
"""
from tests.variables import sb_link
from pages.GT2.pages.confirm_and_deny_page import ConfirmAndDenyCounterparty, ConfirmAndDenyDriver, ConfirmAndDenyVehicle
from pages.GT2.pages.elements import ElementsPage
import pytest


#@pytest.mark.
def test_confirm_new_counterparty_and_deny_after(browser_auth_sb):
    page = ConfirmAndDenyCounterparty(browser_auth_sb, sb_link)
    page.open()
    #page.


@pytest.mark.confirm_driver
def test_confirm_new_driver_and_deny_after(browser_auth_sb):
    page = ConfirmAndDenyDriver(browser_auth_sb, sb_link)
    page.open()
    page.manager_should_confirm_new_driver()


#@pytest.mark.
def test_confirm_new_vehicle_and_deny_after(browser_auth_sb):
    page = ConfirmAndDenyVehicle(browser_auth_sb, sb_link)
    page.open()
    #page.
