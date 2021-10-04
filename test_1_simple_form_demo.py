from selenium import webdriver
import pytest
from BaseClass import BaseClass


class TestSimpleFormDemo(BaseClass):
    
    def test_single_input_field(self):
        url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
        self.driver.get(url)
        message = "hellow world"
        self.driver.find_elements_by_xpath("//input[@id='user-message']")[0].send_keys(message)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Show Message')]")[0].click()
        user_message = self.driver.find_element_by_css_selector("#user-message #display").text
        assert user_message == message


    def test_two_input_fields(self):
        url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
        self.driver.get(url)
        num1 = 2
        num2 = 10
        self.driver.find_element_by_id("sum1").send_keys(num1)
        self.driver.find_element_by_id("sum2").send_keys(num2)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Get Total')]")[0].click()
        total = int(self.driver.find_element_by_id("displayvalue").text)
        assert total == (num1 + num2)
