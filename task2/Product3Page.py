from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import BasePage
import CartPage

from Locators import Product3PageLocators


class Product3Page(BasePage.BasePage):

    def add_to_cart(self, quantity):
        try:
            super().set_input(Product3PageLocators.quantity_field, quantity)
            super().get_elem(Product3PageLocators.button_cart).click()
        except:
            raise

    def goto_cart_page(self):
        try:
            super().get_elem(Product3PageLocators.goto_cart_page).click()
            return CartPage.CartPage(self.driver)
        except:
            raise
