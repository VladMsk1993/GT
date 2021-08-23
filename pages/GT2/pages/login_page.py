import time

from pages.GT2.locators.locators import LoginPageLocators
from pages.GT2.pages.base_page import BasePage


class LoginPage(BasePage):
    def login_into_portal(self, login, password):
        assert self.is_element_present(*LoginPageLocators.E_MAIL), "Отсутствует поле 'Емэил'."
        self.browser.find_element(*LoginPageLocators.E_MAIL).send_keys(login)

        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Отсутствует поле 'Пароль'."
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), "Отсутствует кнопка 'Подтвердить'."
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
