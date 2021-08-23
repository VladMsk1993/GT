"""Страница с часто повторяющимися элементами."""
from pages.GT2.locators.locators import MainPageLocators, HeaderLocators
from pages.GT2.pages.base_page import BasePage
import time


class ElementsPage(BasePage):
    """
    Производим открытие основоной страницы (Рабочий стол) в модуле СЭБ.
    В зависимости от кейса вставляем нужные локаторы для переключения по вкладкам (Все\ТС\Водитель\Контрагент) и
    в строку поиска вкладываем нужный поисково запрос. Все эти параметры вводять непосредственоо в файле теста.
    """
    def manager_should_open_unit_page(self, how, what, name):
        """Основная страница СЭБ."""
        assert self.is_element_present(how, what), "Отустствует вкладка 'Водители'."
        self.browser.find_element(how, what).click()
        time.sleep(1)
        assert self.is_element_present(*HeaderLocators.SEARCH), "Отсутсвует поле поиск."
        self.browser.find_element(*HeaderLocators.SEARCH).send_keys(name)

        time.sleep(1)  # Костыль
        assert self.is_element_present(*MainPageLocators.SEARCH_RESULT), "Отсутсвует результат поискового запроса."
        self.browser.find_element(*MainPageLocators.SEARCH_RESULT).click()