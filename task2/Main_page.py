from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import Base_page
import Product1_page
import Cart_page


class Main_page_locators (object):
    to_cart_prod1 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
    to_cart_prod2 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[1]')
    to_cart_prod3 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[3]/button[1]')
    to_cart_prod4 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[3]/button[1]')
    success_alert = (By.CLASS_NAME, 'alert-success')
    goto_product1_page = (
        By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/h4/a')
    goto_product2_page = (
        By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/h4/a')
    goto_cart_page = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')


class Main_page (Base_page.Base_page):

    def to_cart_prod1(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(Main_page_locators.to_cart_prod1).click()
        except:
            raise

    def to_cart_prod2(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(Main_page_locators.to_cart_prod2).click()
        except:
            raise

    def to_cart_prod3(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(Main_page_locators.to_cart_prod3).click()
        except:
            raise

    def to_cart_prod4(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(Main_page_locators.to_cart_prod4).click()
        except:
            raise

    def was_added_to_cart(self):
        try:
            super().get_elem(Main_page_locators.success_alert)
        except:
            raise

    def goto_cart_page(self):
        try:
            super().get_elem(Main_page_locators.goto_cart_page).click()
            return Cart_page.Cart_page(self.driver)
        except:
            raise

    def goto_product1_page(self):
        try:
            super().get_elem(Main_page_locators.goto_product1_page).click()
            return Product1_page.Product1_page(self.driver)
        except:
            raise
