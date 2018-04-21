from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import Base_page
import Main_page


class Checkout_success_page_locators:

    return_to_main_page_btn = (By.XPATH, '//*[@id="content"]/div/div/a')


class Checkout_success_page(Base_page.Base_page):

    def goto_to_main_page(self):
        try:
            super().get_elem(Checkout_success_page_locators.return_to_main_page_btn).click()
            return Main_page.Main_page(self.driver)
        except:
            raise
