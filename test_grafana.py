from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys


class TestGrafana:
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        if self.driver.find_element(By.ID, "user-name").is_displayed():
            assert True
        else:
            assert False

        self.driver.close()

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        if self.driver.find_element(By.ID, "password").is_displayed():
            assert True
        else:
            assert False

        self.driver.close()

    def test_input(self):
        pytest.skip("Skipping for now")
