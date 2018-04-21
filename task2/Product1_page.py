from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import Base_page
import Cart_page


class Product1_page_locators:

    button_cart = (By.ID, 'button-cart')
    quantity_field = (By.NAME, 'quantity')
    goto_cart_page = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')


class Product1_page(Base_page.Base_page):

    def add_to_cart(self, quantity):
        try:
            super().set_input(Product1_page_locators.quantity_field, quantity)
            super().get_elem(Product1_page_locators.button_cart).click()
        except:
            raise

    def goto_cart_page(self):
        try:
            super().get_elem(Product1_page_locators.goto_cart_page).click()
            return Cart_page.Cart_page(self.driver)
        except:
            raise
