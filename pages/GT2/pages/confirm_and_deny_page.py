"""
Осуществляем согласование нового контрагента, водителя, тс. После отправляем их на повторное согласование и отклоняем.
"""
import time
from pages.GT2.pages.elements import ElementsPage
from pages.GT2.locators.locators import CounterpartyPageLocators, ExchangeWindow, DriverPageLocators, MainPageLocators


class ConfirmAndDenyVehicle(ElementsPage):
    def manager_should_confirm_new_vehicle(self):
        pass
    
    def manager_should_send_vehicle_to_repeat_checking(self):
        pass

    def manager_should_deny_confirmed_vehicle(self):
        pass


class ConfirmAndDenyDriver(ElementsPage):
    def manager_should_confirm_new_driver(self):
        self.manager_should_open_unit_page(*MainPageLocators.DRIVERS, "Румянцев Сергей")

        """Карточка водителя."""
        current_status = self.get_text(*DriverPageLocators.STATUS_NEW)
        assert "НОВЫЙ" == current_status, "Статус водителя не 'Новый'."
        assert self.is_element_present(*DriverPageLocators.TAKE_FOR_WORK), "Отсутсвует кнопка 'Взять в работу'."
        self.browser.find_element(*DriverPageLocators.TAKE_FOR_WORK).click()

        time.sleep(10)
        current_status = self.get_text(*DriverPageLocators.STATUS_IN_AGREEING)
        assert "НА СОГЛАСОВНИИ" == current_status, "Статус водителя не 'На соглсовании'."
        assert self.is_element_present(*DriverPageLocators.AGREE_BUTTON), "Отсутствует кнопка 'Согласовать'."
        self.browser.find_element(*DriverPageLocators.AGREE_BUTTON).click()
        time.sleep(1)
        current_status = self.get_text(*DriverPageLocators.STATUS_AGREED)
        assert "СОГЛАСОВАН" == current_status, "Статус водителя не 'Согласован'."
        assert self.is_element_present(*DriverPageLocators.CHANGE_BUTTON), "Отсутствует кнопка 'Изменить'."
        time.sleep(4)

    def manager_should_send_driver_to_repeat_checking(self):
        self.manager_should_open_unit_page(*MainPageLocators.DRIVERS, "Румянцев Сергей")

        """Карточка водителя."""
        current_status = self.get_text(*DriverPageLocators.STATUS_AGREED)
        assert "СОГЛАСОВАН" == current_status, "Статус водителя не 'Согласован'."
        assert self.is_element_present(*DriverPageLocators.CHANGE_BUTTON), "Отсутствует кнопка 'Изменить'."
        self.browser.find_element(*DriverPageLocators.CHANGE_BUTTON).click()

    def manager_should_deny_confirmed_driver(self):
        self.manager_should_open_unit_page(*MainPageLocators.DRIVERS, "Румянцев Сергей")

        """Карточка водителя."""


class ConfirmAndDenyCounterparty(ElementsPage):
    def manager_should_confirm_new_counterparty(self):
        pass

    def manager_should_send_counterparty_to_repeat_checking(self):
        pass

    def manager_should_deny_confirmed_counterparty(self):
        self.manager_should_open_unit_page(*MainPageLocators.COUNTERPARTY, "Ардей")

        """Страница контрагента СЭБ."""
        assert self.is_element_present(*CounterpartyPageLocators.CHANGE_BUTTON), "Отсутсвует кнопка 'Изменить'."
        self.browser.find_element(*CounterpartyPageLocators.CHANGE_BUTTON).click()
        time.sleep(2)

        """Окно Изменений."""
        assert self.is_element_present(*ExchangeWindow.COMMENT_MANAGER), "Отсутсвует поле комментарий для менеджера."
        self.browser.find_element(*ExchangeWindow.COMMENT_MANAGER).send_keys("Не прошёл проверку. Ответ для менеджеру.")

        assert self.is_element_present(*ExchangeWindow.COMMENT_SB), "Отсутсвует поле комментарий для СБ."
        self.browser.find_element(*ExchangeWindow.COMMENT_SB).send_keys("Не прошёл проверку. Ответ для СБ.")
        time.sleep(2)

        assert self.is_element_present(*ExchangeWindow.DENY_BUTTON), "Отсутсвует кнопка 'Отклонить'."
        self.browser.find_element(*ExchangeWindow.DENY_BUTTON).click()
        time.sleep(2)

        assert self.is_element_present(*ExchangeWindow.DENY_BUTTON), "Отсутсвует кнопка 'Изменить'."
        self.browser.find_element(*ExchangeWindow.DENY_BUTTON).click()