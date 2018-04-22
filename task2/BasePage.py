from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_elem(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(locator))
        except:
            raise

    def set_input(self, locator, input):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(locator))
            elem.clear()
            elem.send_keys(input)
        except:
            raise

    def has_attribute(self, obj, attribute, attr_name):
        try:
            WebDriverWait(self.driver, 10).until(lambda s:
                                                 attr_name in obj.get_attribute(attribute).split())
        except:
            raise
