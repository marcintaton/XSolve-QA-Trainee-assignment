import unittest
from selenium import webdriver

from Main_page import Main_page


class Tests (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://rekrutacjaqa2.xsolve.software/")

    def test_case1(self):
        try:
            main_page = Main_page(self.driver)
            main_page.to_cart_prod3(2)
            product1_page = main_page.goto_product1_page()

            product1_page.add_to_cart(5)
            cart_page = product1_page.goto_cart_page()

            checkout_page = cart_page.goto_checkout()

            checkout_page.guest_step1_mark_guest()
            checkout_page.guest_step1_continue()

            checkout_page.guest_step2_fill_form({
                "Name": "name",
                "Last_name": "lastname",
                "E_Mail": "mail@domain.com",
                "Phone": "phonenum",
                "Company": "Compayny inc.",
                "Adress1": "AD1",
                "Adress2": "AD2",
                "City": "City",
                "Post_code": "Post code",
                "Country": "Peru",
                "State": "Lima"
            })
            checkout_page.guest_step2_is_shipping_billing_adr_change()
            checkout_page.guest_step2_continue()

            checkout_page.guest_step3_fill_form({
                "Name": "name2",
                "Last_name": "lastname2",
                "Company": "Compayny inc222.",
                "Adress1": "AD12",
                "Adress2": "AD22",
                "City": "City2",
                "Post_code": "Post code2",
                "Country": "Poland",
                "State": "Slaskie"
            })
            checkout_page.guest_step3_continue()

            checkout_page.guest_step4_add_comment("Comment sdfdsf")
            checkout_page.guest_step4_continue()

            checkout_page.guest_step5_add_comment("OTher comment")
            checkout_page.guest_step5_terms_and_cond_checkbox_click()
            checkout_page.guest_step5_continue()

            checkout_success_page = checkout_page.guest_step6_submit()

            main_page = checkout_success_page.goto_to_main_page()

        except:
            self.fail()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
