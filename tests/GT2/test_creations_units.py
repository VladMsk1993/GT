"""
В этом тесте с начало выполняется имперсонализация, а после:
1. Создание контрагента в SRM.
2. Создание Водителя в карточке только что созданого контрагента.
3. Создание Грузовика в карточке только что созданого контрагента.
4. Создание Прицепа в карточке только что созданого контрагента.
"""
from pages.GT2.pages.admin_page import AdminPage
from pages.GT2.pages.srm_counterparty_page import CounterParty
from pages.GT2.pages.create_counterparty_page import CreateCounterParty
from pages.GT2.pages.create_truck_page import CreateTruck
from pages.GT2.pages.create_trailer_page import CreateTrailer
from pages.GT2.pages.create_driver_page import CreateDriver
from tests.variables import admin_link
import pytest


@pytest.mark.regress
@pytest.mark.create_counterparty
def test_create_counterparty(browser_auth_srm, browser):
    page = AdminPage(browser_auth_srm, admin_link)
    page.open()
    page.find_manager()
    page = CounterParty(browser, "")
    page.manager_should_open_window_creation_counterparty()
    page = CreateCounterParty(browser, "")
    page.manager_should_create_new_counterparty()


@pytest.mark.regress
@pytest.mark.create_truck
def test_create_truck(browser_auth_srm, browser):
    page = AdminPage(browser_auth_srm, admin_link)
    page.open()
    page.find_manager()
    page = CounterParty(browser, "")
    page.manager_should_go_to_counterparty_window()
    page = CreateTruck(browser, "")
    page.manager_should_create_truck()


@pytest.mark.regress
@pytest.mark.create_trailer
def test_create_trailer(browser_auth_srm, browser):
    page = AdminPage(browser_auth_srm, admin_link)
    page.open()
    page.find_manager()
    page = CounterParty(browser, "")
    page.manager_should_go_to_counterparty_window()
    page = CreateTrailer(browser, "")
    page.manager_should_create_trailer()


@pytest.mark.regress
@pytest.mark.create_driver
def test_create_driver(browser_auth_srm, browser):
    page = AdminPage(browser_auth_srm, admin_link)
    page.open()
    page.find_manager()
    page = CounterParty(browser, "")
    page.manager_should_go_to_counterparty_window()
    page = CreateDriver(browser, "")
    page.manager_should_create_driver()
