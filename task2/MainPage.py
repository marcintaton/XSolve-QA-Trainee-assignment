import BasePage
import Product1Page
import CartPage

from Locators import MainPageLocators


class MainPage (BasePage.BasePage):

    def to_cart_prod1(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(MainPageLocators.to_cart_prod1).click()
        except:
            raise

    def to_cart_prod2(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(MainPageLocators.to_cart_prod2).click()
        except:
            raise

    def to_cart_prod3(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(MainPageLocators.to_cart_prod3).click()
        except:
            raise

    def to_cart_prod4(self, quantity):
        try:
            for _ in range(quantity):
                super().get_elem(MainPageLocators.to_cart_prod4).click()
        except:
            raise

    def was_added_to_cart(self):
        try:
            super().get_elem(MainPageLocators.success_alert)
        except:
            raise

    def goto_cart_page(self):
        try:
            super().get_elem(MainPageLocators.goto_cart_page).click()
            return CartPage.CartPage(self.driver)
        except:
            raise

    def goto_product1_page(self):
        try:
            super().get_elem(MainPageLocators.goto_product1_page).click()
            return Product1Page.Product1Page(self.driver)
        except:
            raise
