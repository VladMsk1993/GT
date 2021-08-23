"""Панель администратора, осуществление имперсонализациию"""

import time
from pages.GT2.pages.base_page import BasePage
from pages.GT2.locators.locators import AdminPageLocators
from tests.variables import main_link, manager_name


class AdminPage(BasePage):
    def find_manager(self):
        assert self.is_element_present(*AdminPageLocators.USERS_BUTTON), "Отсутствует кнопка левого меню (админка) 'Users'"
        self.browser.find_element(*AdminPageLocators.USERS_BUTTON).click()

        assert self.is_element_present(*AdminPageLocators.SEARCH), "Отсутствует поиск (админка)"
        self.browser.find_element(*AdminPageLocators.SEARCH).send_keys(manager_name)

        assert self.is_element_present(*AdminPageLocators.SEACRH_BOTTUN), "Отсутсвтует кнопка поиска (админка)"
        self.browser.find_element(*AdminPageLocators.SEACRH_BOTTUN).click()

        assert self.is_element_present(*AdminPageLocators.IMPERSIONATE_BUTTON), "Отсутствует кнопка имперонализации у менеджера."
        self.browser.find_element(*AdminPageLocators.IMPERSIONATE_BUTTON).click()
        self.change_window(-1)
        self.browser.get(main_link)
