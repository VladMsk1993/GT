"""
Хедер в модуле СЭБ.
"""
import time
from pages.GT2.locators.locators import HeaderLocators, MainPageLocators
from pages.GT2.pages.elements import ElementsPage
from tests.variables import GBDD_url, RSA_url, ati_url, focus_url


class HeaderLinks(ElementsPage):
    def should_check_headers_links_in_vehicle(self):
        self.manager_should_open_unit_page(*MainPageLocators.VEHICLE, "267562")

        """Карточка ТС."""
        assert self.is_element_present(*HeaderLocators.GBDD_BUTTON), "Отсутсвует кнопка 'ГИБДД'."
        self.browser.find_element(*HeaderLocators.GBDD_BUTTON).click()
        self.change_window(-1)
        url = self.get_current_url()
        assert GBDD_url in url, "Ссылка ГИБДД не соответсвует."
        self.change_window(0)

        assert self.is_element_present(*HeaderLocators.RSA_BUTTON), "Отсутсвует кнопка 'РСА'."
        self.browser.find_element(*HeaderLocators.RSA_BUTTON).click()
        self.change_window(-1)
        url = self.get_current_url()
        assert RSA_url in url, "Ссылка РСА не соответсвует."

    def should_check_headers_links_in_driver(self):
        self.manager_should_open_unit_page(*MainPageLocators.DRIVERS, "Румянцев Сергей")

        """Карточка Водителя."""
        assert self.is_not_element_present(*HeaderLocators.RSA_BUTTON), "Кнопка 'РСА' присутсвует, хотя не должна!!!"
        assert self.is_element_present(*HeaderLocators.GBDD_BUTTON), "Отсутсвует кнопка 'ГИБДД'."
        self.browser.find_element(*HeaderLocators.GBDD_BUTTON).click()
        self.change_window(-1)
        url = self.get_current_url()
        assert GBDD_url in url, "Ссылка ГИБДД не соответсвует."

    def should_check_headers_links_in_counterparty(self):
        self.manager_should_open_unit_page(*MainPageLocators.COUNTERPARTY, "Ардей")

        """Страница контрагента СЭБ."""
        assert self.is_element_present(*HeaderLocators.KONTUR_FOCUS_LINK), "Отсутсвует ссылка 'КонтурФокус'."
        self.browser.find_element(*HeaderLocators.KONTUR_FOCUS_LINK).click()
        self.change_window(-1)
        url = self.get_current_url()
        assert focus_url in url, "Ссылка КонтурФокус не соответсвует."
        self.change_window(0)

        assert self.is_element_present(*HeaderLocators.ATISU_LINK), "Отсутсвует ссылка 'КонтурФокус'."
        self.browser.find_element(*HeaderLocators.ATISU_LINK).click()
        self.change_window(-1)
        url = self.get_current_url()
        assert ati_url in url, "Ссылка КонтурФокус не соответсвует."
