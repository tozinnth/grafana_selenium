from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys


class TestGrafana:
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com")
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/img").is_displayed():
            assert True
        else:
            assert False

        self.driver.close()

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, 'q').send_keys("seleniumtest")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
        if self.driver.title == "Grafana":
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

    def test_input(self):
        pytest.skip("Skipping for now")
