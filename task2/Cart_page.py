from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import Base_page
import Checkout_page


class Cart_page_locators:

    checkout_btn = (By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')


class Cart_page(Base_page.Base_page):

    def goto_checkout(self):
        try:
            super().get_elem(Cart_page_locators.checkout_btn).click()
            return Checkout_page.Checkout_page(self.driver)
        except:
            raise
