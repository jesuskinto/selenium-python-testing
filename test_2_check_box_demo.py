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
        assert checkbox.is_selected()
        assert self.driver.find_element_by_id('txtAge').is_displayed()


    def test_two_input_fields(self):
        # Check the below points before automating

        url = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
        self.driver.get(url)
        checkboxs = self.driver.find_elements_by_css_selector(".cb1-element")

        # Click on 'Check All' to check all checkboxes at once.
        self.driver.find_element_by_id("check1").click()
        for checkbox in checkboxs: assert checkbox.is_selected()

        # When you check all the checkboxes, button will change to 'Uncheck All'
        assert (self.driver.find_element_by_id("check1").get_attribute('value') == 'Uncheck All')

        # When you uncheck at least one checkbox, button will change to 'Check All'
        checkboxs[0].click()
        assert (self.driver.find_element_by_id("check1").get_attribute('value') == 'Check All')

        assert True
