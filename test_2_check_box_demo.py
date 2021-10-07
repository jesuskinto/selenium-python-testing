# This would be a basic example to start with checkboxes using selenium.

# The HTML input "checkbox" is an input element to enter an array of different
# values. Eash input type checkbox has value attribute which is used to define
# the value submitted by the checkbox.

from selenium import webdriver
import pytest
from BaseClass import BaseClass


class TestCheckBoxDemo(BaseClass):
    

    def test_single_checkbox_demo(self):
        
        # Clicking on the checkbox will display a success message. Keep an eye on it

        url = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
        self.driver.get(url)
        checkbox = self.driver.find_elements_by_id("isAgeSelected")[0]
        checkbox.click()
        if not checkbox.is_selected(): assert False
        checkbox = self.driver.find_elements_by_id("isAgeSelected")[0]
        assert self.driver.find_element_by_id('txtAge').is_displayed()


    def test_two_input_fields(self):

        # Check the below points before automating

        url = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
        self.driver.get(url)
        checkboxs = self.driver.find_elements_by_css_selector(".cb1-element")

        # Click on 'Check All' to check all checkboxes at once.
        self.driver.find_element_by_id("check1").click()
        for checkbox in checkboxs:
            if not checkbox.is_selected():
                assert False

        # When you check all the checkboxes, button will change to 'Uncheck All'
        if (self.driver.find_element_by_id("check1").get_attribute('value') != 'Uncheck All'):
            assert False

        # When you uncheck at least one checkbox, button will change to 'Check All'
        checkboxs[0].click()
        if (self.driver.find_element_by_id("check1").get_attribute('value') != 'Check All'):
            assert False

        assert True
