import BasePage
import CartPage

from Locators import Product1PageLocators


class Product1Page(BasePage.BasePage):

    def add_to_cart(self, quantity):
        try:
            super().set_input(Product1PageLocators.quantity_field, quantity)
            super().get_elem(Product1PageLocators.button_cart).click()
        except:
            raise

    def goto_cart_page(self):
        try:
            super().get_elem(Product1PageLocators.goto_cart_page).click()
            return CartPage.CartPage(self.driver)
        except:
            raise
