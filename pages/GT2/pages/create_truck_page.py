"""
Страница создания нового Тягоча\малотонажника на странице контрагента (SRM).
"""
import time
from pages.GT2.pages.base_page import BasePage
from pages.GT2.locators.locators import CreateAutoLocators
from tests.variables import *


class CreateTruck(BasePage):
    def manager_should_create_truck(self):
        """Открыто карточка КА."""
        assert self.is_element_present(*CreateAutoLocators.TS_LINK), "Отсутствует кнопка 'Транспортные средства'"
        self.browser.find_element(*CreateAutoLocators.TS_LINK).click()

        self.browser.implicitly_wait(5)

        assert self.is_element_present(*CreateAutoLocators.CREATE_BUTTON), "Отсутсвует кнопка добавить новое ТС."
        self.browser.find_element(*CreateAutoLocators.CREATE_BUTTON).click()
        time.sleep(5)

        """Открыто окно добавления 'Новое транспортное средство'."""
        assert self.is_element_present(*CreateAutoLocators.TRUCK_RADIO), "Отсутствует радиобатан 'Тягач\Малотонажник'"
        self.browser.find_element(*CreateAutoLocators.TRUCK_RADIO).click()

        assert self.is_element_present(*CreateAutoLocators.CONFIRM_BUTTON1), "Отсутствует кнопка 'Начать'."
        self.browser.find_element(*CreateAutoLocators.CONFIRM_BUTTON1).click()

        """Открыто окно добавления с параметрами 'Новый Тягач\малотонажник'."""
        assert self.is_element_present(*CreateAutoLocators.DOWNLOAD_DOCUMENT1), "Отсутствует кнопка загрузки документа 1."
        self.browser.find_element(*CreateAutoLocators.DOWNLOAD_DOCUMENT1).send_keys()

        assert self.is_element_present(*CreateAutoLocators.DOWNLOAD_DOCUMENT2), "Отсутствует кнопка загрузки документа 2."
        self.browser.find_element(*CreateAutoLocators.DOWNLOAD_DOCUMENT2).send_keys()

        assert self.is_element_present(*CreateAutoLocators.SERIA_AREA1), "Отсутствует поле 'Серия' 1."
        self.browser.find_element(*CreateAutoLocators.SERIA_AREA1).send_keys(seria_number)

        assert self.is_element_present(*CreateAutoLocators.NOMBER_AREA1), "Отсутствует поле 'Номер' 1."
        self.browser.find_element(*CreateAutoLocators.NOMBER_AREA1).send_keys(passport_number)

        assert self.is_element_present(*CreateAutoLocators.DATA_GIVEN1), "Отсутствует поле 'Дата выдачи' 1."
        self.browser.find_element(*CreateAutoLocators.DATA_GIVEN1).send_keys(date)

        assert self.is_element_present(*CreateAutoLocators.GIVEN_BY1), "Отсутствует поле 'Кем выдан' 1."
        self.browser.find_element(*CreateAutoLocators.GIVEN_BY1).send_keys()

        assert self.is_element_present(*CreateAutoLocators.DOWNLOAD_DOCUMENT3), "Отсутствует кнопка загрузки документа 3."
        self.browser.find_element(*CreateAutoLocators.DOWNLOAD_DOCUMENT3).send_keys()

        assert self.is_element_present(*CreateAutoLocators.DOWNLOAD_DOCUMENT4), "Отсутствует кнопка загрузки документа 4."
        self.browser.find_element(*CreateAutoLocators.DOWNLOAD_DOCUMENT4).send_keys()

        assert self.is_element_present(*CreateAutoLocators.SERIA_AREA2), "Отсутствует поле 'Серия' 2."
        self.browser.find_element(*CreateAutoLocators.SERIA_AREA2).send_keys(seria_number)

        assert self.is_element_present(*CreateAutoLocators.NOMBER_AREA2), "Отсутствует поле 'Номер' 2."
        self.browser.find_element(*CreateAutoLocators.NOMBER_AREA2).send_keys(passport_number)

        assert self.is_element_present(*CreateAutoLocators.DATA_GIVEN2), "Отсутствует поле 'Дата выдачи' 2."
        self.browser.find_element(*CreateAutoLocators.DATA_GIVEN2).send_keys(date)

        assert self.is_element_present(*CreateAutoLocators.GIVEN_BY2), "Отсутствует поле 'Кем выдан' 2."
        self.browser.find_element(*CreateAutoLocators.GIVEN_BY2).send_keys()

        assert self.is_element_present(*CreateAutoLocators.CONFIRM_BUTTON2), "Отсутствует кнопка подтверждения 'Далее'."
        self.browser.find_element(*CreateAutoLocators.CONFIRM_BUTTON2).click()

        """Открыто окно добавления 'Общая информация'."""
        assert self.is_element_present(*CreateAutoLocators.MARK_AUTO), "Отсутствует поле 'Марка'."
        self.browser.find_element(*CreateAutoLocators.MARK_AUTO).send_keys()

        assert self.is_element_present(*CreateAutoLocators.GOV_NUMBER), "Отсутствует поле 'Государственный номер'."
        self.browser.find_element(*CreateAutoLocators.GOV_NUMBER).send_keys(gov_number)

        assert self.is_element_present(*CreateAutoLocators.VIN_NUMBER), "Отсутствует поле 'VIN номер'."
        self.browser.find_element(*CreateAutoLocators.VIN_NUMBER).send_keys()

        assert self.is_element_present(*CreateAutoLocators.YEAR_PRODUCTION), "Отсутствует поле 'Год производства ТС'."
        self.browser.find_element(*CreateAutoLocators.YEAR_PRODUCTION).send_keys()

        assert self.is_element_present(*CreateAutoLocators.CONFIRM_BUTTON3), "Отсутствует кнопка подтверждения 'Добавить'."
        self.browser.find_element(*CreateAutoLocators.CONFIRM_BUTTON3).click()