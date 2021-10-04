# JQuery Date Picker Demo
# Table consisting of two TextBoxes one for selecting the Start (From) date while other for selecting the End (To) date.
# 
# Start Date should be less than End date
# Start Date and the dates before the Start Date disabled in the End Date
# End Date and the dates after the End Date disabled in the Start Date


import pytest
import time
import re
from selenium import webdriver
from BaseClass import BaseClass


class TestJqueryDate(BaseClass):
    
    def test_jquery_date_picker(self):
        url = "https://www.seleniumeasy.com/test/jquery-date-picker-demo.html"
        self.driver.get(url)
        datepicker = self.driver.find_element_by_id('ui-datepicker-div')
        input_from = self.driver.find_element_by_id('from')
        input_from.click()
        datepicker.find_element_by_xpath("//a[contains(text(),5)]").click()
        input_to = self.driver.find_element_by_id('to')
        input_to.click()
        datepicker.find_element_by_xpath("//a[contains(text(),20)]").click()
        valid_from = re.search("/05/", input_from.get_attribute('value'))
        valid_to = re.search("/20/", input_to.get_attribute('value'))
        assert valid_from and valid_to


    def test_jquery_date_picker_disabled_before(self):
        url = "https://www.seleniumeasy.com/test/jquery-date-picker-demo.html"
        self.driver.get(url)
        datepicker = self.driver.find_element_by_id('ui-datepicker-div')
        
        input_from = self.driver.find_element_by_id('from')
        input_from.click()
        datepicker.find_element_by_xpath("//a[contains(text(),10)]").click()

        input_to = self.driver.find_element_by_id('to')
        input_to.click()
        disabled_elements = datepicker.find_elements_by_css_selector("span.ui-state-default")

        for disable_element in disabled_elements:
            if (int(disable_element.get_attribute('innerText')) >= 10 ):
                assert False

        assert True

    def test_jquery_date_picker_disabled_after(self):
        url = "https://www.seleniumeasy.com/test/jquery-date-picker-demo.html"
        self.driver.get(url)
        datepicker = self.driver.find_element_by_id('ui-datepicker-div')
        
        input_to = self.driver.find_element_by_id('to')
        input_to.click()
        datepicker.find_element_by_xpath("//a[contains(text(),10)]").click()

        input_from = self.driver.find_element_by_id('from')
        input_from.click()
        disabled_elements = datepicker.find_elements_by_css_selector("span.ui-state-default")

        for disable_element in disabled_elements:
            if (int(disable_element.get_attribute('innerText')) <= 10 ):
                assert False
                
        assert True