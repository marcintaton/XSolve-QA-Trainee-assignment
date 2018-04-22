import BasePage
import CheckoutPage

from Locators import CartPageLocators


class CartPage(BasePage.BasePage):

    def goto_checkout(self):
        try:
            super().get_elem(CartPageLocators.checkout_btn).click()
            return CheckoutPage.CheckoutPage(self.driver)
        except:
            raise
