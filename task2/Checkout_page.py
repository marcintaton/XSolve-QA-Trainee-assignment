from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import Base_page
import Checkout_success_page


class Checkout_page_locators:

    step1_collapse = (By.ID, 'collapse-checkout-option')
    step1_guest_checkout_radio = (
        By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
    step1_continue = (By.ID, 'button-account')

    step2_collapse = (By.ID, 'collapse-payment-address')
    step2_name = (By.ID, 'input-payment-firstname')
    step2_last_name = (By.ID, 'input-payment-lastname')
    step2_email = (By.ID, 'input-payment-email')
    step2_phone = (By.ID, 'input-payment-telephone')
    step2_company = (By.ID, 'input-payment-company')
    step2_adress_1 = (By.ID, 'input-payment-address-1')
    step2_adress_2 = (By.ID, 'input-payment-address-2')
    step2_city = (By.ID, 'input-payment-city')
    step2_post_code = (By.ID, 'input-payment-postcode')
    step2_country = (By.ID, 'input-payment-country')
    step2_state = (By.ID, 'input-payment-zone')
    step2_button_guest = (By.ID, 'button-guest')
    step2_shipping_adr_chechbox = (
        By.XPATH, '//*[@id="collapse-payment-address"]/div/div[2]/label/input')
    step2_continue = (By.ID, 'button-guest')

    step3_collapse = (By.ID, 'collapse-shipping-address')
    step3_name = (By.ID, 'input-shipping-firstname')
    step3_last_name = (By.ID, 'input-shipping-lastname')
    step3_company = (By.ID, 'input-shipping-company')
    step3_adress_1 = (By.ID, 'input-shipping-address-1')
    step3_adress_2 = (By.ID, 'input-shipping-address-2')
    step3_city = (By.ID, 'input-shipping-city')
    step3_post_code = (By.ID, 'input-shipping-postcode')
    step3_country = (By.ID, 'input-shipping-country')
    step3_state = (By.ID, 'input-shipping-zone')
    step3_continue = (By.ID, 'button-guest-shipping')

    step4_collapse = (By.ID, 'collapse-shipping-method')
    step4_comment_area = (
        By.XPATH, '//*[@id="collapse-shipping-method"]/div/p[4]/textarea')
    step4_continue = (By.ID, 'button-shipping-method')

    step5_collapse = (By.ID, 'collapse-payment-method')
    step5_comment_area = (
        By.XPATH, '//*[@id="collapse-payment-method"]/div/p[3]/textarea')
    step5_terms_and_cond_checkbox = (By.NAME, 'agree')
    step5_terms_and_cond_link = (By.CLASS_NAME, 'agree')
    step5_continue = (By.ID, 'button-payment-method')

    step6_collapse = (By.ID, 'collapse-checkout-confirm')
    step6_submit = (By.ID, 'button-confirm')


class Checkout_page(Base_page.Base_page):

    def guest_step1_mark_guest(self):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step1_collapse), "in")
            super().get_elem(Checkout_page_locators.step1_guest_checkout_radio).click()
        except:
            raise

    def guest_step1_continue(self):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step1_collapse), "in")
            super().get_elem(Checkout_page_locators.step1_continue).click()
        except:
            raise

    def guest_step2_fill_form(self, input):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step2_collapse), "in")
            super().set_input(Checkout_page_locators.step2_name, input['Name'])
            super().set_input(
                Checkout_page_locators.step2_last_name, input['Last_name'])
            super().set_input(
                Checkout_page_locators.step2_email, input['E_Mail'])
            super().set_input(
                Checkout_page_locators.step2_phone, input['Phone'])
            super().set_input(
                Checkout_page_locators.step2_company, input['Company'])
            super().set_input(
                Checkout_page_locators.step2_adress_1, input['Adress1'])
            super().set_input(
                Checkout_page_locators.step2_adress_2, input['Adress2'])
            super().set_input(Checkout_page_locators.step2_city, input['City'])
            super().set_input(
                Checkout_page_locators.step2_post_code, input['Post_code'])
            Select(super().get_elem(Checkout_page_locators.step2_country)
                   ).select_by_visible_text(input['Country'])
            self.driver.implicitly_wait(1)
            Select(super().get_elem(Checkout_page_locators.step2_state)
                   ).select_by_visible_text(input['State'])
        except:
            raise

    def guest_step2_is_shipping_billing_adr_change(self):
        try:
            super().get_elem(Checkout_page_locators.step2_shipping_adr_chechbox).click()
        except:
            raise

    def guest_step2_continue(self):
        super().has_class(super().get_elem(Checkout_page_locators.step2_collapse), "in")
        super().get_elem(Checkout_page_locators.step2_continue).click()

    def guest_step3_fill_form(self, input):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step3_collapse), "in")
            super().set_input(Checkout_page_locators.step3_name, input['Name'])
            super().set_input(
                Checkout_page_locators.step3_last_name, input['Last_name'])
            super().set_input(
                Checkout_page_locators.step3_company, input['Company'])
            super().set_input(
                Checkout_page_locators.step3_adress_1, input['Adress1'])
            super().set_input(
                Checkout_page_locators.step3_adress_2, input['Adress2'])
            super().set_input(Checkout_page_locators.step3_city, input['City'])
            super().set_input(
                Checkout_page_locators.step3_post_code, input['Post_code'])
            Select(super().get_elem(Checkout_page_locators.step3_country)
                   ).select_by_visible_text(input['Country'])
            self.driver.implicitly_wait(1)
            Select(super().get_elem(Checkout_page_locators.step3_state)
                   ).select_by_visible_text(input['State'])
        except:
            raise

    def guest_step3_continue(self):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step3_collapse), "in")
            super().get_elem(Checkout_page_locators.step3_continue).click()
        except:
            raise

    def guest_step4_add_comment(self, input):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step4_collapse), "in")
            super().set_input(Checkout_page_locators.step4_comment_area, input)
        except:
            raise

    def guest_step4_continue(self):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step4_collapse), "in")
            super().get_elem(Checkout_page_locators.step4_continue).click()
        except:
            raise

    def guest_step5_add_comment(self, input):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step5_collapse), "in")
            super().set_input(Checkout_page_locators.step5_comment_area, input)
        except:
            raise

    def guest_step5_terms_and_cond_checkbox_click(self):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step5_collapse), "in")
            super().get_elem(Checkout_page_locators.step5_terms_and_cond_checkbox).click()
        except:
            raise

    def guest_step5_continue(self):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step5_collapse), "in")
            super().get_elem(Checkout_page_locators.step5_continue).click()
        except:
            raise

    def guest_step6_submit(self):
        try:
            super().has_class(super().get_elem(Checkout_page_locators.step6_collapse), "in")
            super().get_elem(Checkout_page_locators.step6_submit).click()
            return Checkout_success_page.Checkout_success_page(self.driver)
        except:
            raise
