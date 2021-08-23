"""
Страница создания нового перевозчика, которая открывается со страницы "Перевозчкик" SRM нажатием на кнопку "Добавить"
"""
import time
from pages.GT2.locators.locators import CreateCounterPartyPageLocators
from pages.GT2.pages.base_page import BasePage
from tests.variables import inn_number, bic_number, checking_account, email, phone_number, address, inn_date


class CreateCounterParty(BasePage):
    def manager_should_create_new_counterparty(self):
        """Страница ввода ИНН."""
        assert self.is_element_present(*CreateCounterPartyPageLocators.INN_AREA), "Отсутсвует поле ввода ИНН."
        self.browser.find_element(*CreateCounterPartyPageLocators.INN_AREA).send_keys(inn_date)
        time.sleep(1)
        self.input_text_key_return(*CreateCounterPartyPageLocators.INN_AREA, inn_date)

        self.browser.implicitly_wait(1)
        assert self.is_element_present(*CreateCounterPartyPageLocators.START_BUTTON), "Отсутствует кнопка 'Начать'."
        self.browser.find_element(*CreateCounterPartyPageLocators.START_BUTTON).click()
        time.sleep(3)

        """Старница ввода реквизитов."""
        assert self.is_element_present(*CreateCounterPartyPageLocators.BIK_AREA), "Отсутсвует поле ввода BIK."
        self.browser.find_element(*CreateCounterPartyPageLocators.BIK_AREA).send_keys(bic_number)
        time.sleep(3)

        assert self.is_element_present(*CreateCounterPartyPageLocators.CHECKING_ACCOUNT), "Отсутсвует поле ввода 'Расчётный счёт'."
        self.browser.find_element(*CreateCounterPartyPageLocators.CHECKING_ACCOUNT).send_keys(checking_account)

        assert self.is_element_present(*CreateCounterPartyPageLocators.CONFIRM_BUTTON1), "Отсутсвует кнопка 'Далее'."
        self.browser.find_element(*CreateCounterPartyPageLocators.CONFIRM_BUTTON1).click()
        time.sleep(3)

        """Страница ввода личных данных."""
        assert self.is_element_present(*CreateCounterPartyPageLocators.EMAIL_AREA)
        self.browser.find_element(*CreateCounterPartyPageLocators.EMAIL_AREA).send_keys(email)

        assert self.is_element_present(*CreateCounterPartyPageLocators.PHONE_AREA)
        self.browser.find_element(*CreateCounterPartyPageLocators.PHONE_AREA).send_keys(phone_number)

        assert self.is_element_present(*CreateCounterPartyPageLocators.CONFIRM_BUTTON2)
        self.browser.find_element(*CreateCounterPartyPageLocators.CONFIRM_BUTTON2).click()

        """Страница ввода автотранспорта."""
        assert self.is_element_present(*CreateCounterPartyPageLocators.GARAGE_ADDRESS)
        self.browser.find_element(*CreateCounterPartyPageLocators.EMAIL_AREA).send_keys(address)

        assert self.is_element_present(*CreateCounterPartyPageLocators.CONFIRM_BUTTON3)
        self.browser.find_element(*CreateCounterPartyPageLocators.CONFIRM_BUTTON3).click()
