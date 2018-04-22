import BasePage
import MainPage

from Locators import CheckoutSuccessPageLocators


class CheckoutSuccessPage(BasePage.BasePage):

    def goto_main_page(self):
        try:
            super().get_elem(CheckoutSuccessPageLocators.return_to_main_page_btn).click()
            return MainPage.MainPage(self.driver)
        except:
            raise
