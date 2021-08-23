"""
Окно проверки спектрум, в модуле СЭБ.
"""
import time
from pages.GT2.locators.locators import HeaderLocators, MainPageLocators, SpectrumLocators
from pages.GT2.pages.elements import ElementsPage


class CheckInSpectrum(ElementsPage):
    def sb_should_check_driver_in_spectrum(self):
        self.manager_should_open_unit_page(*MainPageLocators.DRIVERS, "Румянцев Сергей")

        """Карточка Водителя, переход в спектрум."""
        assert self.is_element_present(*HeaderLocators.SPECTRUM_BUTTON), "Отсутсвует кнопка 'Spectrum'."
        self.browser.find_element(*HeaderLocators.SPECTRUM_BUTTON).click()

        """Проверка по паспорту."""
        assert self.is_element_present(*SpectrumLocators.CHECK_BUTTON), "Отсутсвует кнопка 'Проверить'."
        self.browser.find_element(*SpectrumLocators.CHECK_BUTTON).click()
        self.browser.implicitly_wait(1)
        assert self.is_element_present(*SpectrumLocators.GOOD_RESULT_CHECKING), "Отсутвует текст с положительным результатом запроса"
        time.sleep(5)
        """Проверка по ВУ,"""
        assert self.is_element_present(*SpectrumLocators.LICENSE_PAGE), "Отсутсвует вкладка 'Водительское удостоверение'."
        self.browser.find_element(*SpectrumLocators.LICENSE_PAGE).click()
        time.sleep(2)

        assert self.is_element_present(*SpectrumLocators.CHECK_BUTTON), "Отсутсвует кнопка 'Проверить'."
        self.browser.find_element(*SpectrumLocators.CHECK_BUTTON).click()
        self.browser.implicitly_wait(1)
        assert self.is_element_present(*SpectrumLocators.GOOD_RESULT_CHECKING), "Отсутвует текст с положительным результатом запроса"

        assert self.is_element_present(*SpectrumLocators.CLOSE_BUTTON), "Отсутсвует крестик"
        self.browser.find_element(*SpectrumLocators.CLOSE_BUTTON).click()
        time.sleep(5)

        """Необходимо брать данные со страницы юнита (паспортные и ВУ) и в носить их в спектрум."""

    def sb_should_check_vehicle_in_spectrum(self):
        self.manager_should_open_unit_page(*MainPageLocators.VEHICLE, "267562")

        """Карточка ТС, переход в спектрум."""
        assert self.is_element_present(*HeaderLocators.SPECTRUM_BUTTON), "Отсутсвует кнопка 'Spectrum'."
        self.browser.find_element(*HeaderLocators.SPECTRUM_BUTTON).click()

        """Проверка по ВИН-номеру."""
        assert self.is_element_present(*SpectrumLocators.CHECK_BUTTON), "Отсутсвует кнопка 'Проверить'."
        self.browser.find_element(*SpectrumLocators.CHECK_BUTTON).click()
        self.browser.implicitly_wait(1)
        assert self.is_element_present(*SpectrumLocators.GOOD_RESULT_CHECKING), "Отсутвует текст с положительным результатом запроса"
        time.sleep(5)

        assert self.is_element_present(*SpectrumLocators.CLOSE_BUTTON), "Отсутсвует крестик"
        self.browser.find_element(*SpectrumLocators.CLOSE_BUTTON).click()
        time.sleep(5)
