"""
Процесс создания нового водителя в модуле SRM.
"""
import os.path
import time
import test_files
from pages.GT2.pages.base_page import BasePage
from pages.GT2.locators.locators import CreateDriverLocators


class CreateDriver(BasePage):
    def manager_should_create_driver(self):
        """Открыто карточка КА."""
        assert self.is_element_present(*CreateDriverLocators.DRIVER_LINK), "Отсутсвует кнопка 'Водители' на странице контрагента."
        self.browser.find_element(*CreateDriverLocators.DRIVER_LINK).click()

        assert self.is_element_present(*CreateDriverLocators.CREATE_BUTTON), "Отсутсвует кнопка 'Добавить водителя' на странице контрагента."
        self.browser.find_element(*CreateDriverLocators.CREATE_BUTTON).click()
        time.sleep(4)

        """Открыто окно добавления 'Новый водитель'."""
        """assert self.is_element_present(*CreateDriverLocators.DOWNLOAD_DOCUMENT1), "Отсутствует кнопка загрузки документа 1."
        self.browser.find_element(*CreateDriverLocators.DOWNLOAD_DOCUMENT1).click()"""
        time.sleep(2)

        assert self.is_element_present(*CreateDriverLocators.DOWNLOAD_DOCUMENT1), "Отсутствует кнопка загрузки документа 2."
        download_doc1 = self.browser.find_element(*CreateDriverLocators.DOWNLOAD_DOCUMENT1)
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'pas.jpeg')
        download_doc1.send_keys(file_path)
        time.sleep(3)

        assert self.is_element_present(*CreateDriverLocators.SERIA_AREA1), "Отсутствует поле 'Серия' 1."
        self.browser.find_element(*CreateDriverLocators.SERIA_AREA1).send_keys()

        assert self.is_element_present(*CreateDriverLocators.NOMBER_AREA1), "Отсутствует поле 'Номер' 1."
        self.browser.find_element(*CreateDriverLocators.NOMBER_AREA1).send_keys()

        assert self.is_element_present(*CreateDriverLocators.DATA_GIVEN1), "Отсутствует поле 'Дата выдачи' 1."
        self.browser.find_element(*CreateDriverLocators.DATA_GIVEN1).send_keys()

        assert self.is_element_present(*CreateDriverLocators.GIVEN_BY1), "Отсутствует поле 'Кем выдан' 1."
        self.browser.find_element(*CreateDriverLocators.GIVEN_BY1).send_keys()

        assert self.is_element_present(*CreateDriverLocators.DOWNLOAD_DOCUMENT3), "Отсутствует кнопка загрузки документа 3."
        self.browser.find_element(*CreateDriverLocators.DOWNLOAD_DOCUMENT3).send_keys()

        assert self.is_element_present(*CreateDriverLocators.DOWNLOAD_DOCUMENT4), "Отсутствует кнопка загрузки документа 4."
        self.browser.find_element(*CreateDriverLocators.DOWNLOAD_DOCUMENT4).send_keys()

        assert self.is_element_present(*CreateDriverLocators.SERIA_AREA2), "Отсутствует поле 'Серия' 2."
        self.browser.find_element(*CreateDriverLocators.SERIA_AREA2).send_keys()

        assert self.is_element_present(*CreateDriverLocators.NOMBER_AREA2), "Отсутствует поле 'Номер' 2."
        self.browser.find_element(*CreateDriverLocators.NOMBER_AREA2).send_keys()

        assert self.is_element_present(*CreateDriverLocators.DATA_GIVEN2), "Отсутствует поле 'Дата выдачи' 2."
        self.browser.find_element(*CreateDriverLocators.DATA_GIVEN2).send_keys()

        assert self.is_element_present(*CreateDriverLocators.GIVEN_BY2), "Отсутствует поле 'Кем выдан' 2."
        self.browser.find_element(*CreateDriverLocators.GIVEN_BY2).send_keys()

        assert self.is_element_present(*CreateDriverLocators.CONFIRM_BUTTON1), "Отсутствует кнопка подтверждения 'Далее'."
        self.browser.find_element(*CreateDriverLocators.CONFIRM_BUTTON1).click()

        """Открыто окно добавления 'Общая информация'."""
        assert self.is_element_present(*CreateDriverLocators.FIRST_NAME), "Отсутствует поле 'Фамилия."
        self.browser.find_element(*CreateDriverLocators.FIRST_NAME).send_keys()

        assert self.is_element_present(*CreateDriverLocators.SECOND_NAME), "Отсутствует поле 'Имя."
        self.browser.find_element(*CreateDriverLocators.SECOND_NAME).send_keys()

        assert self.is_element_present(*CreateDriverLocators.FATHER_NAME), "Отсутствует поле 'Отчество'."
        self.browser.find_element(*CreateDriverLocators.FATHER_NAME).send_keys()

        assert self.is_element_present(*CreateDriverLocators.BIRTHDAY_DATE), "Отсутствует поле 'Дата рождения'."
        self.browser.find_element(*CreateDriverLocators.BIRTHDAY_DATE).send_keys()

        assert self.is_element_present(*CreateDriverLocators.PHONE_NUMBER), "Отсутствует поле 'Телефон'."
        self.browser.find_element(*CreateDriverLocators.PHONE_NUMBER).send_keys()

        assert self.browser.find_element(*CreateDriverLocators.CONFIRM_BUTTON2), "Отсутсвует кнопка 'Добавить'."
        self.browser.find_element(*CreateDriverLocators.CONFIRM_BUTTON2).click()
