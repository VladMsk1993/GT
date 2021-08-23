"""
Основное левое меню в модуле СЭБ.
"""
from pages.GT2.pages.base_page import BasePage
from pages.GT2.locators.locators import LeftMenuLocators, LoginPageLocators
from tests.variables import sb_link


class CheckLeftMenu(BasePage):
    def should_check_buttons_in_left_menu(self):
        assert self.is_element_present(*LeftMenuLocators.WORK_PAGE), "Отсутсвует страница Контрагенты."
        assert self.is_element_present(*LeftMenuLocators.COUNTEPARTY_BUTTON), "Отсутсвует кнопка справочника в левом меню."
        self.browser.find_element(*LeftMenuLocators.COUNTEPARTY_BUTTON).click()

        assert self.is_element_present(*LeftMenuLocators.COUNTEPARTY_PAGE), "Отсутсвует страница Контрагенты."
        assert self.is_element_present(*LeftMenuLocators.WORK_PAGE_BUTTON), "Отсутсвует кнопка справочника в левом меню."
        self.browser.find_element(*LeftMenuLocators.WORK_PAGE_BUTTON).click()

        assert self.is_element_present(*LeftMenuLocators.ELASTIC_BUTTON), "Отсутсвует кнопка Дашборда в левом меню."
        self.browser.find_element(*LeftMenuLocators.ELASTIC_BUTTON).click()
        self.change_window(sb_link, 0)

        assert self.is_element_present(*LeftMenuLocators.EXIT_BUTTON), "Отсутсвует кнопка выхода в левом меню."
        self.browser.find_element(*LeftMenuLocators.EXIT_BUTTON).click()

        """Страница авторизации."""
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), "Отсутствует кнопка 'Войти'."
