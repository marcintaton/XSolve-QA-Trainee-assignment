from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import Base_page


class Login_page_locators (object):
    e_mail = (By.ID, "input-email")
    password = (By.ID, "input-password")
    login_button = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')


class Login_page (Base_page.Base_page):

    def title_test(self):
        return "Account Login" in self.driver.title

    def type_email(self, input):
        self.driver.find_element(
            *Login_page_locators.e_mail).send_keys(input)

    def type_password(self, input):
        self.driver.find_element(
            *Login_page_locators.password).send_keys(input)

    def login(self, email, password):
        self.driver.find_element(
            *Login_page_locators.e_mail).send_keys(email)
        self.driver.find_element(
            *Login_page_locators.password).send_keys(password)
        self.driver.find_element(
            *Login_page_locators.login_button).click()
