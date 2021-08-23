"""
Осуществляем отклонение нового контрагента, водителя, тс. После отправляем их на повторное согласование и согласовываем.
"""
import time
from pages.GT2.pages.elements import ElementsPage
from pages.GT2.locators.locators import MainPageLocators, HeaderLocators, CounterpartyPageLocators, ExchangeWindow


class DenyAndConfirmCounterparty(ElementsPage):
    def manager_should_deny_new_counterparty(self):
        pass

    def manager_should_send_counterparty_to_repeat_checking(self):
        pass

    def manager_should_confirm_denied_counterparty(self):
        pass


class DenyAndConfirmVehicle(ElementsPage):
    def manager_should_deny_new_vehicle(self):
        pass

    def manager_should_send_vehicle_to_repeat_checking(self):
        pass

    def manager_should_confirm_denied_vehicle(self):
        pass


class DenyAndConfirmDriver(ElementsPage):
    def manager_should_deny_new_driver(self):
        pass

    def manager_should_send_driver_to_repeat_checking(self):
        pass

    def manager_should_confirm_denied_driver(self):
        pass


