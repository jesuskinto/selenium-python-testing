# Bootstrap Modal Example for Automation

from selenium import webdriver
import pytest
import time

from BaseClass import BaseClass


class TestBoostrapModals(BaseClass):

    def test_single_modal(self):
        url = "https://www.seleniumeasy.com/test/bootstrap-modal-demo.html"
        self.driver.get(url)
        modal = self.driver.find_element_by_xpath("//a[@href='#myModal0']")
        modal.click()
        modal_body_text = self.driver.find_element_by_css_selector("#myModal0 .modal-body").get_attribute('innerText')
        assert modal_body_text.strip() == 'This is the place where the content for the modal dialog displays'


    def test_multiple_modal(self):
        # This is the place where the content for the modal dialog displays.
        # Click launch modal button to launch second modal.
        # Click close link to close the modal.
        # Clicking on Save Changes button will close the modal and refresh the page

        url = "https://www.seleniumeasy.com/test/bootstrap-modal-demo.html"
        self.driver.get(url)
        button_open_modal = self.driver.find_element_by_xpath("//a[@href='#myModal']")
        button_open_modal.click()
        modal = self.driver.find_element_by_id("myModal")
        time.sleep(3)
        assert modal.is_displayed()
