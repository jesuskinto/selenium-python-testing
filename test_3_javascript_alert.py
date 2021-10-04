from selenium import webdriver
import pytest
from BaseClass import BaseClass


class TestJavascriptAlerts(BaseClass):
    
    def test_javascript_alert_box(self):
        url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
        self.driver.get(url)
        button = self.driver.find_elements_by_css_selector(".btn.btn-default")[0]
        button.click()
        alert_box = self.driver.switch_to.alert
        message = alert_box.text
        alert_box.accept()
        assert 'I am an alert box!' == message


    def test_javascript_confirm_box(self):
        url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
        self.driver.get(url)
        button = self.driver.find_elements_by_css_selector(".btn.btn-default")[1]
        button.click()
        alert_box = self.driver.switch_to.alert
        message = alert_box.text
        alert_box.accept()
        assert 'Press a button!' == message


    def test_javascript_confirm_box_accept(self):
        url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
        self.driver.get(url)
        button = self.driver.find_elements_by_css_selector(".btn.btn-default")[1]
        button.click()
        alert_box = self.driver.switch_to.alert
        alert_box.accept()
        confirm_text = self.driver.find_element_by_id('confirm-demo').text
        assert confirm_text == 'You pressed OK!'


    def test_javascript_confirm_box_cancel(self):
        url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
        self.driver.get(url)
        button = self.driver.find_elements_by_css_selector(".btn.btn-default")[1]
        button.click()
        alert_box = self.driver.switch_to.alert
        alert_box.dismiss()
        confirm_text = self.driver.find_element_by_id('confirm-demo').text
        assert confirm_text == 'You pressed Cancel!'


    def test_javascript_prompt_box(self):
        url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"
        self.driver.get(url)
        message = 'Hi'
        button = self.driver.find_elements_by_css_selector(".btn.btn-default")[2]
        button.click()
        alert_box = self.driver.switch_to.alert
        alert_box.send_keys(message)
        alert_box.accept()
        confirm_text = self.driver.find_element_by_id('prompt-demo').text
        assert confirm_text == f"You have entered '{message}' !"
