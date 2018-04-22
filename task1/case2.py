import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class Registration_form_with_after_party (unittest.TestCase):

    # A very simple test class for performing tests on registration form
    # and choosing after-party option

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
        # Assuming that "First name" field in the form has name "first name". I will assume other fields' names in similar fashion
        # Finding elements by their names and sending input
        driver.find_element_by_name("first_name").send_keys("Name")
        driver.find_element_by_name("last_name").send_keys("Surname")
        driver.find_element_by_name("company").send_keys("Company")
        driver.find_element_by_name("email").send_keys("")
        # Finding and checking checkbox button
        driver.find_element_by_name("after-party").click()
        # Choosing an option from food preferences dropdown list
        Select(driver.find_element_by_name('food-preferences')
               ).select_by_visible_text('Vegetarian')
        # Finding phone number element sending input
        driver.find_element_by_name("phone").send_keys("4567891432")
        # Finding and clicking submit button
        driver.find_element_by_name("submit").click()
        # Let us assume that after successfull form submition we are reditected to a confirmation page with different title than original page
        try:
            WebDriverWait(driver, 15).until_not(EC.title_is(title),
                                                "Timeout while waiting for confirmation page")
        finally:
            self.fail()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
