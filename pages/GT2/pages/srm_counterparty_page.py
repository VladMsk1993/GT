"""Страница "Перевозчики" SRM."""
import time
from pages.GT2.pages.base_page import BasePage
from pages.GT2.locators.locators import CounterPartyPageLocators
from tests.variables import counterparty_name


class CounterParty(BasePage):
    def manager_should_open_window_creation_counterparty(self):
        assert self.is_element_present(*CounterPartyPageLocators.COUNTERPARTY_BUTTON), "Отсутствует кнопка справочника."
        self.browser.find_element(*CounterPartyPageLocators.COUNTERPARTY_BUTTON).click()

        assert self.is_element_present(*CounterPartyPageLocators.BUTTON_CREATE_COUNTERPARTY), "Отсутствет кнопка 'Добавить контрагента'"
        self.browser.find_element(*CounterPartyPageLocators.BUTTON_CREATE_COUNTERPARTY).click()

    def manager_should_go_to_counterparty_window(self):
        assert self.is_element_present(*CounterPartyPageLocators.COUNTERPARTY_BUTTON), "Отсутствует кнопка справочника."
        self.browser.find_element(*CounterPartyPageLocators.COUNTERPARTY_BUTTON).click()

        assert self.is_element_present(*CounterPartyPageLocators.SEARCH_AREA), "Отсутствует поле поиска."
        self.browser.find_element(*CounterPartyPageLocators.SEARCH_AREA).send_keys(counterparty_name)

        time.sleep(1)   # Котстыльик, необходимо заменить.

        search_result = self.browser.find_element(*CounterPartyPageLocators.THE_RESULT).text
        assert self.is_element_present(*CounterPartyPageLocators.THE_RESULT), "Отсутствует результат поискового запроса."

        assert counterparty_name in search_result, "Результат поискового запроса не соответствует запросу."
        self.browser.find_element(*CounterPartyPageLocators.THE_RESULT).click()

    def manager_should_add_docs_and_send_counterparty_for_agreement(self):
        assert self.is_element_present(*CounterPartyPageLocators.DOCUMENT_LINK), "Отсутствует кнопка левого меню 'Документы'."
        self.browser.find_element(*CounterPartyPageLocators.DOCUMENT_LINK).click()

        assert self.is_element_present(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT1), "Отсутствует поле загрузки документа 1."
        self.browser.find_element(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT1).send_keys()

        assert self.is_element_present(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT2), "Отсутствует поле загрузки документа 2."
        self.browser.find_element(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT2).send_keys()

        assert self.is_element_present(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT3), "Отсутствует поле загрузки документа 3."
        self.browser.find_element(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT3).send_keys()

        assert self.is_element_present(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT4), "Отсутствует поле загрузки документа 4."
        self.browser.find_element(*CounterPartyPageLocators.DOWNLOAD_DOCUMENT4).send_keys()

        assert self.is_element_present(*CounterPartyPageLocators.AGREEMENT_LINK), "Отсутствует кнопка левого меню 'Согласование'."
        self.browser.find_element(*CounterPartyPageLocators.AGREEMENT_LINK).click()

        assert self.is_element_present(*CounterPartyPageLocators.AGREEMENT_BUTTON), "Отсутствует кнопка отправки КА на 'Согласование'."
        self.browser.find_element(*CounterPartyPageLocators.AGREEMENT_BUTTON).click()
