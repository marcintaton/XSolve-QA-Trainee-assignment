import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Registration_form_no_after_party (unittest.TestCase):

    # A simple test class for performing tests on registration form
    # without choosing after-party option

    def setUp(self):
        # Opening a browser to carry out test
        self.driver = webdriver.Chrome()

    def test_form_sumbission(self):
        driver = self.driver
        # Assuming that this is registration form's web adress
        driver.get("https://www.registrationform.fun")
        # Assuming that page title should be "Registreation" and checking for it
        self.assertIn("Registration", driver.title)
        # Saving current page title
        title = driver.title
        # Making sure that registration form has loaded (assuming that it's id is "registration_form")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'registration_form')))
        finally:
            self.tearDown()

        # Assuming that "First name" field in the form has name "first name". I will assume other fields' names in similar fashion
        # Finding elements by their names, making sure they exist and sending input
        try:
            driver.find_element_by_name("first_name").send_keys("Name")
        except NoSuchElementException:
            self.tearDown()

        try:
            driver.find_element_by_name("last_name").send_keys("Surname")
        except NoSuchElementException:
            self.tearDown()

        try:
            driver.find_element_by_name("company").send_keys("Company")
        except NoSuchElementException:
            self.tearDown()

        try:
            driver.find_element_by_name("email").send_keys("")
        except NoSuchElementException:
            self.tearDown()

        # Finding and clicking submit button
        try:
            driver.find_element_by_name("submit").click()
        except NoSuchElementException:
            self.tearDown()

        # Let us assume that after successfull form submition we are reditected to a confirmation page with different title than original page

        WebDriverWait(driver, 15,).until_not(EC.title_is(title),
                                             "Timeout while waiting for confirmation page")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
