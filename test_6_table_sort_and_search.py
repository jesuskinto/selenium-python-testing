from selenium import webdriver
import pytest
from BaseClass import BaseClass


class TestTableSortAndSearch(BaseClass):
    
    def test_template(self):
        url = "https://www.seleniumeasy.com/test/bootstrap-modal-demo.html"
        self.driver.get(url)
        assert True