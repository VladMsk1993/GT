import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def input_text_key_return(self, how, what, text):
        try:
            element = self.browser.find_element(how, what)
            element.send_keys(text)
            element.send_keys(Keys.RETURN)
        except NoSuchElementException:
            return False
        return True

    def change_window(self, num):
        work_window = self.browser.window_handles[0]
        time.sleep(0.5)
        opened_window = self.browser.window_handles[num]
        self.browser.switch_to.window(opened_window)

    def get_current_url(self):
        """ Returns current browser URL. """
        return self.browser.current_url

    def get_text(self, how, what):
        """ Get text of the element. """
        element = self.browser.find_element(how, what)
        text = str(element.text)
        return text

    def get_attribute(self, attr_name):
        """ Get attribute of the element. """
        element = self.browser.find_element()
        if element:
            return element.get_attribute(attr_name)
