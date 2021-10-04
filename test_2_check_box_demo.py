from selenium import webdriver
import pytest
from BaseClass import BaseClass


class TestCheckBoxDemo(BaseClass):
    

    def test_single_checkbox_demo(self):
        url = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
        self.driver.get(url)
        checkbox = self.driver.find_elements_by_id("isAgeSelected")[0]
        checkbox.click()
        assert checkbox.is_selected()


    def test_two_input_fields(self):
        url = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
        self.driver.get(url)
        checkboxs = self.driver.find_elements_by_css_selector(".cb1-element")
        
        count = 0
        for checkbox in checkboxs:
            checkbox.click()
            if checkbox.is_selected():
                count +=1 

        assert len(checkboxs) == count
