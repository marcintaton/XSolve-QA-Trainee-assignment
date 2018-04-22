import BasePage

from Locators import LoginPageLocators


class LoginPage (BasePage.BasePage):

    def login(self, email, password):
        try:
            super().set_input(LoginPageLocators.e_mail, input)
            super().set_input(LoginPageLocators.password, input)
            super().get_elem(LoginPageLocators.login_button).click()
        except:
            raise
