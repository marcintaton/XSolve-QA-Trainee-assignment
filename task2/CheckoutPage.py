from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import BasePage
import CheckoutSuccessPage

from Locators import CheckoutPageLocators


class CheckoutPage(BasePage.BasePage):

    def guest_step1_mark_guest(self):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step1_collapse), "class", "in")
            super().get_elem(CheckoutPageLocators.step1_guest_checkout_radio).click()
        except:
            raise

    def guest_step1_continue(self):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step1_collapse), "class", "in")
            super().get_elem(CheckoutPageLocators.step1_continue).click()
        except:
            raise

    def guest_step2_fill_form(self, input):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step2_collapse), "class", "in")
            super().set_input(CheckoutPageLocators.step2_name, input['Name'])
            super().set_input(
                CheckoutPageLocators.step2_last_name, input['Last_name'])
            super().set_input(
                CheckoutPageLocators.step2_email, input['E_Mail'])
            super().set_input(
                CheckoutPageLocators.step2_phone, input['Phone'])
            super().set_input(
                CheckoutPageLocators.step2_company, input['Company'])
            super().set_input(
                CheckoutPageLocators.step2_adress_1, input['Adress1'])
            super().set_input(
                CheckoutPageLocators.step2_adress_2, input['Adress2'])
            super().set_input(CheckoutPageLocators.step2_city, input['City'])
            super().set_input(
                CheckoutPageLocators.step2_post_code, input['Post_code'])
            Select(super().get_elem(CheckoutPageLocators.step2_country)
                   ).select_by_visible_text(input['Country'])
            self.driver.implicitly_wait(1)
            Select(super().get_elem(CheckoutPageLocators.step2_state)
                   ).select_by_visible_text(input['State'])
        except:
            raise

    def guest_step2_is_shipping_billing_adr_change(self):
        try:
            super().get_elem(CheckoutPageLocators.step2_shipping_adr_chechbox).click()
        except:
            raise

    def guest_step2_continue(self):
        super().has_attribute(super().get_elem(
            CheckoutPageLocators.step2_collapse), "class", "in")
        super().get_elem(CheckoutPageLocators.step2_continue).click()

    def guest_step3_fill_form(self, input):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step3_collapse), "class", "in")
            super().set_input(CheckoutPageLocators.step3_name, input['Name'])
            super().set_input(
                CheckoutPageLocators.step3_last_name, input['Last_name'])
            super().set_input(
                CheckoutPageLocators.step3_company, input['Company'])
            super().set_input(
                CheckoutPageLocators.step3_adress_1, input['Adress1'])
            super().set_input(
                CheckoutPageLocators.step3_adress_2, input['Adress2'])
            super().set_input(CheckoutPageLocators.step3_city, input['City'])
            super().set_input(
                CheckoutPageLocators.step3_post_code, input['Post_code'])
            Select(super().get_elem(CheckoutPageLocators.step3_country)
                   ).select_by_visible_text(input['Country'])
            self.driver.implicitly_wait(1)
            Select(super().get_elem(CheckoutPageLocators.step3_state)
                   ).select_by_visible_text(input['State'])
        except:
            raise

    def guest_step3_continue(self):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step3_collapse), "class", "in")
            super().get_elem(CheckoutPageLocators.step3_continue).click()
        except:
            raise

    def guest_step4_add_comment(self, input):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step4_collapse), "class", "in")
            super().set_input(CheckoutPageLocators.step4_comment_area, input)
        except:
            raise

    def guest_step4_continue(self):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step4_collapse), "class", "in")
            super().get_elem(CheckoutPageLocators.step4_continue).click()
        except:
            raise

    def guest_step5_add_comment(self, input):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step5_collapse), "class", "in")
            super().set_input(CheckoutPageLocators.step5_comment_area, input)
        except:
            raise

    def guest_step5_terms_and_cond_checkbox_click(self):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step5_collapse), "class", "in")
            super().get_elem(CheckoutPageLocators.step5_terms_and_cond_checkbox).click()
        except:
            raise

    def guest_step5_continue(self):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step5_collapse), "class", "in")
            super().get_elem(CheckoutPageLocators.step5_continue).click()
        except:
            raise

    def guest_step6_submit(self):
        try:
            super().has_attribute(super().get_elem(
                CheckoutPageLocators.step6_collapse), "class", "in")
            super().get_elem(CheckoutPageLocators.step6_submit).click()
            return CheckoutSuccessPage.CheckoutSuccessPage(self.driver)
        except:
            raise
